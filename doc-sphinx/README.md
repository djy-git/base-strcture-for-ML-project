# Documentation using [`SPHINX`](https://www.sphinx-doc.org/en/master/) package
Details are in https://www.sphinx-doc.org/en/master/

## Source root directory: `/src`


### 1. Install `sphinx`
    $ pip install sphinx
    $ pip install sphinx-rtd-theme


### 2. Change directory to `doc-sphinx`
    $ cd doc-sphinx


### 3. Initialize project settings
    $ sphinx-quickstart
    
    // Write information of the project 
    
    // 한국어 지원이 필요한 경우 다음을 사용
    // Project language [en]: ko

### 4. Modify configurations
#### 1) `/doc-sphinx/source/conf.py`
1. Add `src` directory to `sys.path`
     
       // Existing
       # import os
       # import sys
       # sys.path.insert(0, os.path.abspath('.'))
       
       // Modified
       import os
       import sys
       sys.path.insert(0, os.path.abspath(
           os.path.join(os.getcwd(), "..", "..", "src")
       ))

2. Add extensions

       // Existing
       extensions = [
       ]
       
       // Modified
       extensions = ['sphinx.ext.autodoc', 'sphinx_rtd_theme']

3. Change html theme

       // Existing
       html_theme = 'alabaster'
       
       // Modified
       html_theme = 'sphinx_rtd_theme'


#### 2) `/doc-sphinx/source/index.rst`
1. Add `modules`
       
       // Existing (Line 9-13)
       .. toctree::
          :maxdepth: 2
          :caption: Contents:
    
       // Modified (Line 9-13)
       .. toctree::
          :maxdepth: 2
          :caption: Contents:
    
          modules
      

### 5. Generate `rst` files (ReStructuredText)
    $ sphinx-apidoc -f -o source ../src
    
    
### 6. Build htmls
    $ make html 
    

### 7. See the generated document in `/doc-sphinx/build/html/index.html`


### 8. Whenever new changes occur, repeat steps 5-7
