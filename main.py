import requests
from bs4 import BeautifulSoup
import argparse
import graphviz


def get_depends(url: str):
    try:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        depends_section = soup.find('summary', string=lambda text: text and "Depends" in text)
        if depends_section: # Если depens существует
            depends_details = depends_section.find_parent('details')
            # Извлекает текст всех тегов <a> внутри списка <ul>
            depends_links = [a.text.strip() for a in depends_details.select('ul.pure-menu-list a')]
            return depends_links
        else:
            return -1  # Ошибка доступа
    except requests.RequestException as e:
        return -2  # Если ошибка по url


def create_graph(package_str, depends_lst):
    dot = graphviz.Digraph(comment='Dependency Graph')
    dot.node(package_str, package_str)
    for dep in depends_lst:
        dot.node(dep, dep)
        dot.edge(dep, package_str)
    dot.format = 'png'
    output_path = dot.render('dependency_graph')
    return output_path

def main():
    # TODO: Сделать поддержку --key для аргументов и добавить аргумент для программы визуализации графа
    parser = argparse.ArgumentParser(description="Dependency graph visualizer for Alpine Linux packages.")
    # parser.add_argument("graph_tool_path", help="Путь к программе для визуализации графов.")
    parser.add_argument("package_name", help="Имя анализируемого пакета.")
    parser.add_argument("repo_url", help="Базовый URL репозитория Alpine Linux.")
    args = parser.parse_args()
    full_url = f"{args.repo_url}/package/edge/main/x86_64/{args.package_name}"
    # Я знаю что такое delete
    depends_lst = get_depends(full_url)
    if depends_lst == -1:
        print(f"Ошибка: не удалось получить зависимости для {args.package_name}.")
    elif depends_lst == -2:
        print("Ошибка. Проверьте URL репозитория.")
    else:
        print(depends_lst)
        package_str = str(args.package_name)
        print(package_str)
        path_picture = create_graph(package_str, depends_lst)
        print(f'Граф создан по пути {path_picture}.')


if __name__ == "__main__":
    main()