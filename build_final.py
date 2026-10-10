import re

def build():
    with open('c:/Users/prana/Desktop/tarun-project/latex.txt', 'r', encoding='utf-8') as f:
        latex_text = f.read()
        
    with open('c:/Users/prana/Desktop/tarun-project/extended_chapters.tex', 'r', encoding='utf-8') as f:
        extended_content = f.read()
        
    with open('c:/Users/prana/Desktop/tarun-project/more_extended_chapters.tex', 'r', encoding='utf-8') as f:
        more_extended_content = f.read()
        
    with open('c:/Users/prana/Desktop/tarun-project/even_more_chapters.tex', 'r', encoding='utf-8') as f:
        even_more_extended_content = f.read()

    # 1. Modify images for cover
    latex_text = latex_text.replace("{vtu.png}", "{images/vtu.png}")
    latex_text = latex_text.replace("{image.png}", "{images/college-logo.png}")
    
    # Define vtuRed color
    latex_text = latex_text.replace("\\definecolor{vtuBrown}{RGB}{139,69,19}", 
                                    "\\definecolor{vtuBrown}{RGB}{139,69,19}\n\\definecolor{vtuRed}{RGB}{192,0,0}")
    
    # Reduce cover page space to fix year spilling
    latex_text = latex_text.replace(r"\begin{center}", r"\begin{center}\vspace*{-1cm}", 1)
    latex_text = latex_text.replace("\\[1cm]\n\n{\\fontsize{14}{17}\\bfseries CAMBRIDGE", "\\[0.2cm]\n\n{\\fontsize{14}{17}\\bfseries CAMBRIDGE")
    latex_text = latex_text.replace("\\[1.5cm]\n\n{\\fontsize{14}{17}", "\\[0.5cm]\n\n{\\fontsize{14}{17}")
    latex_text = latex_text.replace("\\[2cm]\n\n\\includegraphics", "\\[0.5cm]\n\n\\includegraphics")

    # 2. Remove double newpage causing empty page
    empty_page_str = "\\newpage\n\\coverpagefalse\n\n% =============================================================================\n%  CERTIFICATE PAGE\n% =============================================================================\n\\newpage"
    replacement_str = "\\newpage\n\\coverpagefalse\n\n% =============================================================================\n%  CERTIFICATE PAGE\n% =============================================================================\n"
    latex_text = latex_text.replace(empty_page_str, replacement_str)

    # 3. Replace TikZ Border and add Fancyhdr
    old_tikz = r"""% ── TikZ border on every page ─────────────────────────────────────────────────
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{eso-pic}

% Cover page: rounded rectangle; all other pages: sharp rectangle
\newif\ifcoverpage
\coverpagefalse

\AddToShipoutPictureBG{%
  \begin{tikzpicture}[remember picture, overlay]
    \ifcoverpage
      \draw[line width=1.4pt, rounded corners=10pt]
        ([xshift=12pt, yshift=-12pt]current page.north west)
        rectangle
        ([xshift=-12pt, yshift=12pt]current page.south east);
    \else
      \draw[line width=1.2pt]
        ([xshift=14pt, yshift=-14pt]current page.north west)
        rectangle
        ([xshift=-14pt, yshift=14pt]current page.south east);
    \fi
  \end{tikzpicture}%
}"""

    new_tikz_and_fancy = r"""% ── TikZ border and Fancyhdr ─────────────────────────────────────────────────
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{eso-pic}
\usepackage{fancyhdr}
\usepackage{tocloft}
\setlength{\headheight}{15pt}
\renewcommand\cftsecfont{\normalfont}
\renewcommand\cftsecpagefont{\normalfont}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}

\newif\iffrontmatterborder
\frontmatterbordertrue

\AddToShipoutPictureBG{%
  \begin{tikzpicture}[remember picture, overlay]
    \iffrontmatterborder
      \draw[line width=2.0pt]
        ([xshift=20pt, yshift=-20pt]current page.north west)
        rectangle
        ([xshift=-20pt, yshift=20pt]current page.south east);
    \fi
  \end{tikzpicture}%
}

\fancypagestyle{frontmatter}{
    \fancyhf{}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
    \fancyfoot[C]{\vspace{5pt}\thepage}
}

\fancypagestyle{mainmatter}{
    \fancyhf{}
    \fancyhead[C]{\fontsize{10}{12}\selectfont\textbf{CONVOSHOP: RAG FRAMEWORK FOR E-COMMERCE PRODUCT ADVISORY}}
    \fancyfoot[L]{\fontsize{10}{12}\selectfont\textbf{DEPT. OF CSE, CITNC 2025-26}}
    \fancyfoot[R]{\fontsize{10}{12}\selectfont\textbf{Page | \thepage}}
    \renewcommand{\headrulewidth}{1.5pt}
    \renewcommand{\footrulewidth}{1.5pt}
}
"""
    latex_text = latex_text.replace(old_tikz, new_tikz_and_fancy)

    # 4. Enable styles
    latex_text = latex_text.replace(r"\pagenumbering{roman}", "\\pagenumbering{roman}\n\\pagestyle{frontmatter}")
    main_matter_start = r"""% =============================================================================
%  CHAPTER 1 -- INTRODUCTION
% =============================================================================
\pagenumbering{arabic}"""
    main_matter_replace = main_matter_start + "\n\\pagestyle{mainmatter}\n\\frontmatterborderfalse\n"
    latex_text = latex_text.replace(main_matter_start, main_matter_replace)
    
    # 5. Certificate Page changes
    latex_text = latex_text.replace(
        "{\\fontsize{14}{17}\\bfseries CAMBRIDGE INSTITUTE OF TECHNOLOGY NORTH CAMPUS\\\\[3pt]}",
        "\\includegraphics[width=2.5cm]{images/college-logo.png}\\\\[5pt]\n{\\fontsize{14}{17}\\bfseries\\color{vtuBlue} CAMBRIDGE INSTITUTE OF TECHNOLOGY NORTH CAMPUS\\\\[3pt]}"
    )
    latex_text = latex_text.replace(
        "{\\fontsize{14}{17}\\bfseries DEPARTMENT OF COMPUTER SCIENCE \\& ENGINEERING\\\\[1.5cm]}",
        "{\\fontsize{14}{17}\\bfseries\\color{vtuBlue} DEPARTMENT OF COMPUTER SCIENCE \\& ENGINEERING\\\\[0.5cm]}"
    )
    
    latex_text = latex_text.replace("{\\fontsize{12}{15}\\bfseries KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[3pt]}", 
                              "{\\fontsize{12}{15}\\bfseries\\color{vtuBlue} KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[3pt]}")
    latex_text = latex_text.replace("{\\fontsize{12}{15}\\bfseries 2025 -- 2026\\\\[0.5cm]}", 
                              "{\\fontsize{12}{15}\\bfseries\\color{vtuBlue} 2025 -- 2026\\\\[0.5cm]}")
    latex_text = latex_text.replace("{\\fontsize{12}{15}\\bfseries KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[1cm]}", 
                              "{\\fontsize{12}{15}\\bfseries\\color{vtuBlue} KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[0.5cm]}")
                              
    latex_text = latex_text.replace("\\\\[1.5cm]", "\\\\[0.5cm]")
    latex_text = latex_text.replace("\\\\[1cm]", "\\\\[0.5cm]")
    
    latex_text = latex_text.replace(
        "{\\fontsize{16}{20}\\bfseries CERTIFICATE\\\\[0.5cm]}",
        "{\\fontsize{16}{20}\\bfseries\\color{vtuRed} CERTIFICATE\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Certificate}"
    )
    latex_text = latex_text.replace(
        "\\textbf{``ConvoShop: A Retrieval-Augmented Generation Framework for Intent-Driven E-Commerce Product Advisory''}",
        "\\textbf{\\color{vtuRed}``ConvoShop: A Retrieval-Augmented Generation Framework for Intent-Driven E-Commerce Product Advisory''}"
    )
    latex_text = latex_text.replace("\\textbf{DECLARATION}\\\\[0.5cm]}", "\\textbf{DECLARATION}\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Declaration}")
    latex_text = latex_text.replace("\\textbf{ACKNOWLEDGEMENT}\\\\[0.5cm]}", "\\textbf{ACKNOWLEDGEMENT}\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Acknowledgement}")
    latex_text = latex_text.replace("\\textbf{ABSTRACT}\\\\[0.5cm]}", "\\textbf{ABSTRACT}\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Abstract}")

    co_guide_str = r"""\noindent
\begin{minipage}[t]{0.45\textwidth}
\raggedright
\rule{5cm}{0.4pt}\\[6pt]
\textbf{Signature of Co-Guide}\\
\textbf{Prof. Varshini T R}\\
\textbf{Asst. Professor}\\
\textbf{Dept. of CSE, CITNC,}\\
\textbf{Bengaluru}
\end{minipage}

\vspace{0.5cm}

\noindent
\begin{tabular}{@{}p{7cm}@{}p{7cm}@{}}
Name of External 1: \underline{\hspace{5cm}} & Signature: \underline{\hspace{4cm}} \\[14pt]
Name of External 2: \underline{\hspace{5cm}} & Signature: \underline{\hspace{4cm}} \\
\end{tabular}"""

    external_viva_str = r"""\vspace{0.5cm}

{\fontsize{14}{17}\bfseries\color{vtuBlue} External Viva\\[5pt]}
\noindent
\begin{tabular}{@{}p{8cm}@{}p{8cm}@{}}
\textbf{Name of the Examiners} & \textbf{Signature with Date} \\[10pt]
1. \underline{\hspace{6cm}} & \underline{\hspace{5cm}} \\[15pt]
2. \underline{\hspace{6cm}} & \underline{\hspace{5cm}} \\
\end{tabular}"""
    latex_text = latex_text.replace(co_guide_str, external_viva_str)

    # 6. Declaration Page changes
    latex_text = latex_text.replace("\\[15pt]", "\\[5pt]")
    latex_text = latex_text.replace("\\[10pt]\nSoumya", "\\[5pt]\nSoumya")
    
    # 7. TOC Header format
    old_toc_head = r"""\begin{center}
{\fontsize{16}{20}\bfseries TABLE OF CONTENTS\\[10pt]}
\end{center}

\tableofcontents"""
    new_toc_head = r"""\begin{center}
{\fontsize{16}{20}\bfseries TABLE OF CONTENTS\\[10pt]}
\end{center}

\noindent\textbf{Chapter} \hfill \textbf{Chapter Name} \hfill \textbf{Page No.}\par\smallskip\hrule\vspace{10pt}
\renewcommand{\contentsname}{}
\vspace{-1.5cm}
\tableofcontents"""
    latex_text = latex_text.replace(old_toc_head, new_toc_head)
    
    # 8. List of Figures Customization
    old_lof = latex_text[latex_text.find(r"{\fontsize{16}{20}\bfseries LIST OF FIGURES"):latex_text.find(r"{\fontsize{16}{20}\bfseries LIST OF TABLES")]
    new_lof = r"""{\fontsize{16}{20}\bfseries LIST OF FIGURES\\[10pt]}
\end{center}
\addcontentsline{toc}{section}{List of Figures}
\begin{longtable}{@{} c l c @{}}
\textbf{Figure No.} & \textbf{Figure Name} & \textbf{Page No.} \\[10pt]
1.1 & Domain Overview of ConvoShop & \pageref{fig:domain} \\[6pt]
3.1 & System Architecture Diagram & \pageref{fig:arch} \\[6pt]
4.1 & Flowchart of ConvoShop Pipeline & \pageref{fig:pipeline} \\[6pt]
4.2 & Context Fusion and LLM Reasoning & \pageref{fig:context} \\[6pt]
5.1 & Intent Decomposition Process & \pageref{fig:intent} \\[6pt]
5.2 & Semantic Retrieval Graph & \pageref{fig:retrieve} \\[6pt]
\end{longtable}

\newpage
\begin{center}
"""
    latex_text = latex_text.replace(old_lof, new_lof)

    # Add intro to all subsections if followed directly by subsubsection
    latex_text = re.sub(r"(\\subsection\*\{.*?\})\n+(\\subsubsection\*\{.*?\})", 
                     r"\1\nThis section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.\n\n\2", 
                     latex_text)

    # 9. Extract references location and split
    ref_idx = -1
    lines = latex_text.split('\n')
    for i, line in enumerate(lines):
        if 'REFERENCES' in line and r'\begin{center}' in lines[i-1]:
            ref_idx = i - 1
            break
            
    if ref_idx != -1:
        main_content = "\n".join(lines[:ref_idx])
    else:
        main_content = latex_text

    # Append extended content
    main_content += "\n" + extended_content + "\n"
    main_content += "\n" + more_extended_content + "\n"
    main_content += "\n" + even_more_extended_content + "\n"
    
    # Append references
    main_content += r"""
\newpage
\begin{center}
{\fontsize{16}{20}\bfseries REFERENCES\\[10pt]}
\end{center}
\addcontentsline{toc}{section}{References}
\begin{enumerate}
  \item Lewis, P., et al. (2020). Retrieval-Augmented Generation for knowledge-intensive NLP tasks. \textit{Advances in Neural Information Processing Systems}, 33, 9459-9474.
  \item Karpukhin, V., et al. (2020). Dense Passage Retrieval for open-domain question answering. \textit{Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)}, 6769-6781.
  \item Sun, Y., \& Zhang, Y. (2018). Conversational recommender system. \textit{Proceedings of the 41st International ACM SIGIR Conference on Research \& Development in Information Retrieval}, 235-244.
  \item Zhang, Y., et al. (2014). Explicit factor models for explainable recommendation based on phrase-level sentiment analysis. \textit{Proceedings of the 37th International ACM SIGIR Conference}, 83-92.
  \item Shuster, K., et al. (2021). Retrieval augmentation reduces hallucination in conversation. \textit{Findings of the Association for Computational Linguistics: EMNLP 2021}, 3784-3803.
  \item Reimers, N., \& Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. \textit{Proceedings of the 2019 Conference on EMNLP}, 3982-3992.
  \item Gao, Y., et al. (2024). Retrieval-Augmented Generation for large language models: A survey. \textit{arXiv preprint arXiv:2312.10997}.
  \item Ji, Z., et al. (2023). Survey of hallucination in natural language generation. \textit{ACM Computing Surveys}, 55(12), 1-38.
  \item Vaswani, A., et al. (2017). Attention is all you need. \textit{Advances in neural information processing systems}, 30.
  \item Devlin, J., et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. \textit{arXiv preprint arXiv:1810.04805}.
  \item Johnson, J., Douze, M., \& Jégou, H. (2019). Billion-scale similarity search with GPUs. \textit{IEEE Transactions on Big Data}, 7(3), 535-547.
  \item Covington, P., Adams, J., \& Sargin, E. (2016). Deep neural networks for YouTube recommendations. \textit{Proceedings of the 10th ACM conference on recommender systems}, 191-198.
  \item Barkan, O., \& Koenigstein, Noam. (2016). Item2vec: neural item embedding for collaborative filtering. \textit{2016 IEEE 26th International Workshop on Machine Learning for Signal Processing (MLSP)}, 1-6.
  \item He, X., et al. (2017). Neural collaborative filtering. \textit{Proceedings of the 26th international conference on world wide web}, 173-182.
\end{enumerate}
\end{document}
"""

    # 10. Table captions
    tables = re.findall(r"(\\begin{table}.*?\\end{table})", main_content, flags=re.DOTALL)
    for table in tables:
        caption_match = re.search(r"(\\caption{.*?})", table)
        if caption_match:
            caption = caption_match.group(1)
            new_table = table.replace(caption, "")
            new_table = new_table.replace(r"\begin{tabular}", caption + "\n" + r"\begin{tabular}")
            new_table = new_table.replace("\n\n\\end{table}", "\n\\end{table}")
            main_content = main_content.replace(table, new_table)
            
    main_content = main_content.replace(r"\caption{Table 5.1: Quantitative Comparison", r"\caption{\textbf{Table 5.1:} Quantitative Comparison")
    
    # 11. Insert 6 Flowchart Tikz Figures
    fig_domain = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=2cm]
\node (user) [rectangle, draw, rounded corners] {User Intent};
\node (rag) [rectangle, draw, rounded corners, right of=user, xshift=2cm] {RAG Engine};
\node (llm) [rectangle, draw, rounded corners, right of=rag, xshift=2cm] {Gemini LLM};
\draw[->, thick] (user) -- (rag);
\draw[->, thick] (rag) -- (llm);
\end{tikzpicture}
\caption{\textbf{Fig 1.1:} Domain Overview of ConvoShop. A high-level view mapping user intent to LLM output.}
\label{fig:domain}
\end{figure}
"""
    main_content = main_content.replace(r"\subsection*{1.1 E-Commerce Background}", r"\subsection*{1.1 E-Commerce Background}" + fig_domain)

    fig_arch = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=1.5cm, every node/.style={rectangle, draw, rounded corners, align=center}]
\node (ui) {React Frontend};
\node (api) [below of=ui, yshift=-0.5cm] {FastAPI Backend};
\node (vec) [below of=api, xshift=-2cm, yshift=-0.5cm] {FAISS Vector DB};
\node (mongo) [below of=api, xshift=2cm, yshift=-0.5cm] {MongoDB};
\draw[<->, thick] (ui) -- (api);
\draw[<->, thick] (api) -- (vec);
\draw[<->, thick] (api) -- (mongo);
\end{tikzpicture}
\caption{\textbf{Fig 3.1:} System Architecture Diagram. Displays the 3-tier architecture with separate vector and document stores.}
\label{fig:arch}
\end{figure}
"""
    main_content = main_content.replace(r"\subsection*{3.1 Hybrid RAG Architecture Overview}", r"\subsection*{3.1 Hybrid RAG Architecture Overview}" + fig_arch)

    fig_pipeline = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=1.5cm, every node/.style={rectangle, draw, rounded corners, align=center}]
\node (input) {Raw Data};
\node (clean) [below of=input] {Cleaning \& Imputation};
\node (embed) [below of=clean] {Vector Embedding (768d)};
\node (index) [below of=embed] {Pinecone Indexing};
\draw[->, thick] (input) -- (clean);
\draw[->, thick] (clean) -- (embed);
\draw[->, thick] (embed) -- (index);
\end{tikzpicture}
\caption{\textbf{Fig 4.1:} Flowchart of ConvoShop Pipeline. The ETL pipeline transforming raw Kaggle datasets into dense embeddings.}
\label{fig:pipeline}
\end{figure}
"""
    main_content = main_content.replace(r"\subsection*{4.1 Data Cleaning and Normalization}", r"\subsection*{4.1 Data Cleaning and Normalization}" + fig_pipeline)

    fig_context = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=2cm, every node/.style={rectangle, draw, rounded corners, align=center}]
\node (q) {User Query};
\node (k) [right of=q, xshift=2cm] {Top-K Products};
\node (fuse) [below of=q, xshift=2cm] {Prompt Template Fusion};
\node (gen) [below of=fuse] {LLM Generation};
\draw[->, thick] (q) -- (fuse);
\draw[->, thick] (k) -- (fuse);
\draw[->, thick] (fuse) -- (gen);
\end{tikzpicture}
\caption{\textbf{Fig 4.2:} Context Fusion and LLM Reasoning. Merging query semantics with exact product metadata.}
\label{fig:context}
\end{figure}
"""
    main_content = main_content.replace(r"\subsection*{4.3 The RAG Context Window}", r"\subsection*{4.3 The RAG Context Window}" + fig_context)

    fig_intent = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=2cm, every node/.style={rectangle, draw, rounded corners, align=center}]
\node (user) {Natural Language};
\node (llm) [right of=user, xshift=2cm] {LLM Parser};
\node (json) [right of=llm, xshift=2cm] {JSON Constraints};
\draw[->, thick] (user) -- (llm);
\draw[->, thick] (llm) -- (json);
\end{tikzpicture}
\caption{\textbf{Fig 5.1:} Intent Decomposition Process. Parsing natural language into strict JSON numerical constraints.}
\label{fig:intent}
\end{figure}
"""
    main_content = main_content.replace(r"\subsection*{5.1 Conversational Chat Interface}", r"\subsection*{5.1 Conversational Chat Interface}" + fig_intent)

    fig_retrieve = r"""
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=2cm, every node/.style={rectangle, draw, rounded corners, align=center}]
\node (db) {Vector Database};
\node (search) [right of=db, xshift=2cm] {Semantic Search};
\node (res) [right of=search, xshift=2cm] {Ranked Results};
\draw[->, thick] (db) -- (search);
\draw[->, thick] (search) -- (res);
\end{tikzpicture}
\caption{\textbf{Fig 5.2:} Semantic Retrieval Graph. Querying the vector space to extract nearest neighbor products.}
\label{fig:retrieve}
\end{figure}
"""
    main_content = main_content.replace(r"\subsection*{5.2 Product Recommendation output}", r"\subsection*{5.2 Product Recommendation output}" + fig_retrieve)

    # Subchapter intros
    main_content = re.sub(r"(\\subsection\*\{.*?\})\n+(\\subsubsection\*\{.*?\})", 
                     r"\1\nThis section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.\n\n\2", 
                     main_content)

    with open('c:/Users/prana/Desktop/tarun-project/Final_Report.tex', 'w', encoding='utf-8') as f:
        f.write(main_content)

if __name__ == '__main__':
    build()
