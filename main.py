import requests
from bs4 import BeautifulSoup
import argparse
import graphviz

def check_url_exists(url: str):
    '''
    Существование репозитория
    :param url: ссылки на репозиторий
    :return: True либо False
    '''
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def get_depends(url: str):
    '''
    Получение зависимостей
    :param url: сслыка на репозиторий
    :return: кортеж зависимостей либо код ошибки
    '''
    try:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        depends_section = soup.find('summary', string=lambda text: text and "Depends" in text)
        if depends_section:
            depends_details = depends_section.find_parent('details')
            # Достает текст всех тегов <a> внутри списка <ul>
            depends_links = [a.text.strip() for a in depends_details.select('ul.pure-menu-list a')]
            return depends_links
        else:
            return -1  # Ошибка доступа
    except requests.RequestException as e:
        return -2  # Если ошибка по url

def create_graph(package_str, depends_lst, graph_tool_path, output_dir):
    '''
    Создает граф
    :param package_str: название пакета
    :param depends_lst: лист зависимостей
    :param output_dir: путь для сохранения графа
    :return: путь к графу
    '''
    dot = graphviz.Digraph(comment='Dependency Graph', format='png', directory=output_dir)
    dot.node(package_str, package_str)
    for dep in depends_lst:
        dep_sanitized = dep.replace(":", "_")  # Потому что graphviz такой крутой и не видет :
        dot.node(dep_sanitized, dep_sanitized)
        dot.edge(dep_sanitized, package_str)
    output_path = dot.render(filename='dependency_graph')
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Dependency graph visualizer for Alpine Linux packages.")
    parser.add_argument("graph_tool_path", help="Путь к программе для визуализации графов.")
    parser.add_argument("package_name", help="Имя анализируемого пакета.")
    parser.add_argument("repo_url", help="Базовый URL репозитория Alpine Linux.")
    args = parser.parse_args()
    output_dir = "graphs"
    full_urls = [
        f"{args.repo_url}/package/edge/main/x86_64/{args.package_name}",
        f"{args.repo_url}/package/edge/community/x86_64/{args.package_name}",
        f"{args.repo_url}/package/edge/testing/x86_64/{args.package_name}"
    ]

    for elem in full_urls:
        if check_url_exists(elem):
            depends_lst = get_depends(elem)
            if depends_lst == -1:
                print(f"Ошибка: не удалось получить зависимости для {args.package_name}.")
            elif depends_lst == -2:
                print("Ошибка. Проверьте URL репозитория.")
            else:
                print(depends_lst)
                package_str = str(args.package_name)
                print(package_str)
                path_picture = create_graph(package_str, depends_lst, args.graph_tool_path, output_dir)
                print(f'Граф создан по пути {path_picture}.')
            exit()
    print(f"В репозиториях main, community, testing нет пакета {args.package_name}.")
    # Я знаю что такое delete

if __name__ == "__main__":
    main()