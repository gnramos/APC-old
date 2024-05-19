import os
import re


ADMONITION_PATTERN = re.compile(r'(!!! +(info|note) +"(.*?)".*?)')
ANCHOR_PATTERN = re.compile(r'\[id> +(.*?)\](\(.*?\))?')
CODE_BLOCK_NL_PATTERN = re.compile(r'``` +linguagem_natural +title="(.*?)".*?[\s\S]([.\s\S]*?)```')
INCLUDE_PATTERN = re.compile(r'[\s\S]{! +(.*?) +!}(?=[\s\S])')
MERMAID_PATTERN = re.compile(r'``` +mermaid +title="(.*?)"([.\s\S]*?)```')
# MY_ADMONITION_PATTERN = re.compile(r'!!! +(\w+) *')
MY_ADMONITION_PATTERN = re.compile(r'(!!! +(\w+)(.*)[\s\S])')#(.*$))')


def add_anchor_to_admonitions(markdown):
    def repl(match):
        content = match.group(1)
        sub = match.group(3).strip()
        return content.replace(sub, f'[id> {sub}]')

    return ADMONITION_PATTERN.sub(repl, markdown)


def code_block_NL(markdown):
    repl = r'<div class="language-text highlight" id="alg-\1">' \
           r'<span class="filename">\1</span>' \
           r'<pre style="white-space: pre-wrap;">' \
           r'<code class="linguagem-natural">\2</code></pre></div>'
    return CODE_BLOCK_NL_PATTERN.sub(repl, markdown)


def my_admonitions(markdown):
    def repl(match):
        full, admonition, extra = match.groups()
        if admonition == 'info' and not extra:
            return '!!! info "Definição"'
        if admonition == 'note' and not extra:
            return '!!! note "Dica"'
        if admonition == 'warning' and not extra:
            return '!!! warning "Atenção"'
        return full

    return MY_ADMONITION_PATTERN.sub(repl, markdown)


def set_anchors(markdown):
    def repl(match):
        text = match.group(1).strip()
        id = text.replace('  ', ' ').replace(' ', '-')
        if match.group(2):
            return f'[<span id="{id}">{text}</span>]{match.group(2)}'
        return f'<span id="{id}">{text}</span>'

    return ANCHOR_PATTERN.sub(repl, markdown)


def on_page_read_source(page, config):
    def repl(match):
        with open(os.path.join('md', match.group(1).strip())) as f:
            content = f.read()
        return f'\n{content}\n'

    with open(os.path.join('md', page.file.src_uri)) as f:
        source = f.read()

    if page.file.src_uri.endswith('.md'):
        while INCLUDE_PATTERN.search(source):
            source = INCLUDE_PATTERN.sub(repl, source)
    return source


def assert_sections(markdown, src_uri):
    quote = r'!!! quote "\[.*?\]\(http.*?\)"[\s\S]{2}( {4}\*\w.*?\*)[\s\S]{2}'
    assert re.search(quote, markdown), f'"{src_uri}" sem citação.'

    intro = r'---[\s\S]{2}(\*\w.*?\*)[\s\S]{2}---'
    assert re.search(intro, markdown), f'"{src_uri}" sem introdução.'

    resumo = r'<h2>Resumo</h2>'
    assert re.search(resumo, markdown), f'"{src_uri}" sem exercícios.'

    exercicios = r'<h2>Exercícios</h2>'
    assert re.search(exercicios, markdown), f'"{src_uri}" sem exercícios.'


def on_page_markdown(markdown, page, config, files):
    # markdown = include_files(markdown)
    markdown = my_admonitions(markdown)
    markdown = add_anchor_to_admonitions(markdown)
    markdown = set_anchors(markdown)
    markdown = code_block_NL(markdown)
    markdown = mermaid_title(markdown)
    src_uri = page.file.src_uri
    if src_uri != index_uri:
        pass
        # assert_sections(markdown, src_uri)
    return markdown


def mermaid_title(markdown):
    repl = r'<div class="language-text highlight" id="\1">' \
           r'<span class="filename">\1</span>\n\n' \
           r'``` mermaid\2```\n\n</div>'
    return MERMAID_PATTERN.sub(repl, markdown)

# # # with open('markdown/pensamento_computacional.md') as f:
# with open('markdown/index.md') as f:
#     markdown = f.read()
#     print(my_admonitions(markdown))


with open('mkdocs.yml') as f:
    index_uri = re.search(r'nav:[\s\S].*?: (.+)', f.read()).group(1)
