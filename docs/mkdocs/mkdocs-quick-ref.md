# MkDocs Quick References

- [配置](https://mkdocs.readthedocs.io/en/0.10/user-guide/configuration/)
- [第三方主题](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)

## Material for MkDocs

### Resources

- [Getting started](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [Reference](https://squidfunk.github.io/mkdocs-material/reference/)

### Install and configuration

=== "install"

    ``` shell
    pip install mkdocs && mkdocs --version
    pip install mkdocs-material
    ```

=== "verification"


    ``` shell
    pip list | grep mkdocs
    mkdocs                             1.3.0
    mkdocs-material                    8.3.3
    mkdocs-material-extensions         1.0.3
    ```

=== "upgrade"

    ``` shell
    pip install --upgrade mkdocs
    pip install --upgrade mkdocs-material
    pip install --upgrade mkdocs-material-extensions
    ```

=== "run"

    ``` shell
    mkdocs serve --dev-addr=0.0.0.0:80  # Run on port 80, accessible over the local network.
    ```

mkdocs.yml中添加:

``` yaml title="mkdocs.yml"
theme:
  name: material
```

### Examples

#### TOC

- [TOC扩展](https://squidfunk.github.io/mkdocs-material/extensions/permalinks/)

```
markdown_extensions:
  - toc:
    permalink: true
```

#### PyMdown Extensions

- [PyMdown Extensions](https://squidfunk.github.io/mkdocs-material/extensions/pymdown/): a collection of Markdown extensions that add some great missing features to the standard Markdown library

#### Admonition

```
!!! warning "警告"
    提示和警告文本: [Admonition](https://squidfunk.github.io/mkdocs-material/extensions/admonition/)
```

!!! warning "警告"
    提示和警告文本: [Admonition](https://squidfunk.github.io/mkdocs-material/extensions/admonition/)

#### Code Snippets

- [highlight.js - Syntax highlighting for the Web](https://highlightjs.org/): 编程语言高亮

``` c
#include <stdio.h>

int main(void) {
  printf("Hello world!\n");
  return 0;
}
```

Tabed Code:

``` yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
```

=== "Code"

    ```
    === "C"

        ``` c
        #include <stdio.h>

        int main(void) {
          printf("Hello world!\n");
          return 0;
        }
        ```

    === "C++"

        ``` c++
        #include <iostream>

        int main(void) {
          std::cout << "Hello world!" << std::endl;
          return 0;
        }
        ```
    ```

=== "Effect"

    === "C"

        ``` c
        #include <stdio.h>

        int main(void) {
          printf("Hello world!\n");
          return 0;
        }
        ```

    === "C++"

        ``` c++
        #include <iostream>

        int main(void) {
          std::cout << "Hello world!" << std::endl;
          return 0;
        }
        ```


#### Arithmatex

- https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#arithmatex

=== "configuration"

    ``` yaml title="mkdocs.yml"
    markdown_extensions:
      - pymdownx.arithmatex:
          generic: true

    extra_javascript:
      - javascripts/mathjax.js
      - https://polyfill.io/v3/polyfill.min.js?features=es6
      - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
    ```

=== "Code"

    ```
    $$
    E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
    $$

    \[3 < 4\]

    \begin{align}
      p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
      p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
    \end{align}
    ```

=== "Effect"

    $$
    E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
    $$

    \[3 < 4\]

    \begin{align}
      p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
      p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
    \end{align}

##### Material

=== "Code"

    ```
    $$
    \underline{\textbf{f}} \texttt{loat}
    \left\{ \begin{array}{l}
     \underline{\textbf{add}} \\
     \underline{\textbf{sub}} \texttt{tract} \\
     \underline{\textbf{mul}} \texttt{tiply} \\
     \underline{\textbf{div}} \texttt{ide} \\
     \underline{\textbf{sq}} \texttt{uare}  \underline{\textbf{r}} \texttt{oo} \underline{\textbf{t}} \\
     \underline{\textbf{min}} \texttt{imum} \\
     \underline{\textbf{max}} \texttt{imum} \\
    \end{array} \right\}
    \left\{ \begin{array}{l}
     \underline{\textbf{.s}} \texttt{ingle} \\
     \underline{\textbf{.d}} \texttt{ouble} \\
    \end{array} \right\}
    $$
    ```

=== "Effect"

    $$
    \underline{\textbf{f}} \texttt{loat}
    \left\{ \begin{array}{l}
     \underline{\textbf{add}} \\
     \underline{\textbf{sub}} \texttt{tract} \\
     \underline{\textbf{mul}} \texttt{tiply} \\
     \underline{\textbf{div}} \texttt{ide} \\
     \underline{\textbf{sq}} \texttt{uare}  \underline{\textbf{r}} \texttt{oo} \underline{\textbf{t}} \\
     \underline{\textbf{min}} \texttt{imum} \\
     \underline{\textbf{max}} \texttt{imum} \\
    \end{array} \right\}
    \left\{ \begin{array}{l}
     \underline{\textbf{.s}} \texttt{ingle} \\
     \underline{\textbf{.d}} \texttt{ouble} \\
    \end{array} \right\}
    $$

##### Github

- [Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
- [LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)
- [MathJax](http://docs.mathjax.org/en/latest/input/tex/index.html#tex-and-latex-support)

=== "Code"

    ````
    $$
    \underline{\textbf{f}} \texttt{loat}
    \begin{Bmatrix*}[l]
     \underline{\textbf{add}} \\
     \underline{\textbf{sub}} \texttt{tract} \\
     \underline{\textbf{mul}} \texttt{tiply} \\
     \underline{\textbf{div}} \texttt{ide} \\
     \underline{\textbf{sq}} \texttt{uare}  \underline{\textbf{r}} \texttt{oo} \underline{\textbf{t}} \\
     \underline{\textbf{min}} \texttt{imum} \\
     \underline{\textbf{max}} \texttt{imum} \\
    \end{Bmatrix*}
    \begin{Bmatrix*}[l]
     \underline{\textbf{.s}} \texttt{ingle} \\
     \underline{\textbf{.d}} \texttt{ouble} \\
    \end{Bmatrix*}
    $$
    ````

=== "Effect"

    $$
    \underline{\textbf{f}} \texttt{loat}
    \begin{Bmatrix*}[l]
     \underline{\textbf{add}} \\
     \underline{\textbf{sub}} \texttt{tract} \\
     \underline{\textbf{mul}} \texttt{tiply} \\
     \underline{\textbf{div}} \texttt{ide} \\
     \underline{\textbf{sq}} \texttt{uare}  \underline{\textbf{r}} \texttt{oo} \underline{\textbf{t}} \\
     \underline{\textbf{min}} \texttt{imum} \\
     \underline{\textbf{max}} \texttt{imum} \\
    \end{Bmatrix*}
    \begin{Bmatrix*}[l]
     \underline{\textbf{.s}} \texttt{ingle} \\
     \underline{\textbf{.d}} \texttt{ouble} \\
    \end{Bmatrix*}
    $$

#### Foot Notes

=== "Code"

    ```
    脚注: [^1]

    [^1]: https://squidfunk.github.io/mkdocs-material/extensions/footnotes/
    ```

=== "Effect"

    脚注: [^1]

    [^1]: https://squidfunk.github.io/mkdocs-material/extensions/footnotes/


#### Mermaid

- [引入mermaid diagrams](https://github.com/squidfunk/mkdocs-material/issues/693):

``` yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_div_format

extra_javascript:
  - https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js
```

```
  ``` mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
  ```
```

``` mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

#### Graphviz

- code: https://github.com/sprin/markdown-inline-graphviz/issues/7


=== "install"

    ```
    pip install markdown-inline-graphviz-extension
    ```

=== "configuration"

    ``` yaml title="mkdocs.yml"
    markdown_extensions:
      - markdown_inline_graphviz
    ```

```
  <div>
  {% dot attack_plan.svg
      digraph G {
          rankdir=LR
          Earth [peripheries=2]
          Mars
          Earth -> Mars
      }
  %}
  </div>
```

<div>
{% dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
%}
</div>
