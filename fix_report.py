import re

def fix_report():
    with open('c:/Users/prana/Desktop/tarun-project/Final_Report.tex', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Cover page year going out of bounds
    # Reduce vertical spacing heavily on cover page
    cover_page = content[:content.find('\\begin{center}\n\n{\\fontsize{14}{17}\\bfseries\\color{vtuBlue} CAMBRIDGE INSTITUTE')]
    cover_page_fixed = cover_page.replace('\\[1cm]', '\\[0.5cm]').replace('\\[1.5cm]', '\\[0.5cm]').replace('\\[2cm]', '\\[1cm]')
    content = cover_page_fixed + content[content.find('\\begin{center}\n\n{\\fontsize{14}{17}\\bfseries\\color{vtuBlue} CAMBRIDGE INSTITUTE'):]

    # 2. Fix Certificate and Declaration colors
    content = content.replace("{\\fontsize{12}{15}\\bfseries KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[3pt]}", 
                              "{\\fontsize{12}{15}\\bfseries\\color{vtuBlue} KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[3pt]}")
    content = content.replace("{\\fontsize{12}{15}\\bfseries 2025 -- 2026\\\\[0.5cm]}", 
                              "{\\fontsize{12}{15}\\bfseries\\color{vtuBlue} 2025 -- 2026\\\\[0.5cm]}")
    
    content = content.replace("{\\fontsize{12}{15}\\bfseries KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[1cm]}", 
                              "{\\fontsize{12}{15}\\bfseries\\color{vtuBlue} KUNDANA, BENGALURU -- 562110, KARNATAKA\\\\[0.5cm]}")
                              
    # 3. Add TOC lines for starting pages
    # Abstract, Acknowledgement, Declaration, Certificate
    content = content.replace("\\textbf{CERTIFICATE}\\\\[0.5cm]}", "\\textbf{CERTIFICATE}\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Certificate}")
    content = content.replace("\\textbf{DECLARATION}\\\\[1cm]}", "\\textbf{DECLARATION}\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Declaration}")
    content = content.replace("\\textbf{ACKNOWLEDGEMENT}\\\\[1cm]}", "\\textbf{ACKNOWLEDGEMENT}\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Acknowledgement}")
    content = content.replace("\\textbf{ABSTRACT}\\\\[1cm]}", "\\textbf{ABSTRACT}\\\\[0.5cm]}\n\\addcontentsline{toc}{section}{Abstract}")

    # 4. TOC Customization (3 columns)
    toc_pattern = r"\\begin{center}\n{\\fontsize{16}{20}\\bfseries TABLE OF CONTENTS.*?\\end{center}"
    new_toc = r"""\begin{center}
{\fontsize{16}{20}\bfseries TABLE OF CONTENTS\\[10pt]}
\end{center}
\addcontentsline{toc}{section}{Table of Contents}
\begin{center}
\textbf{Chapter} \hfill \textbf{Chapter Name} \hfill \textbf{Page No.}
\end{center}
\@starttoc{toc}"""
    # But since we have manual longtable for TOC in latex.txt, let's find it.
    if r"\begin{longtable}{@{} c l c @{}}" in content:
        # User had a manual TOC table! Let's modify it to Chapter | Chapter Name | Page No.
        content = content.replace(r"\textbf{Chapter No.} & \textbf{Chapter Name} & \textbf{Page No.} \\[10pt]", 
                                  r"\textbf{Chapter} & \textbf{Chapter Name} & \textbf{Page No.} \\[10pt]")

    # 5. List of Figures: reduce to 6 important images
    old_lof = content[content.find(r"{\fontsize{16}{20}\bfseries LIST OF FIGURES\\[10pt]}"):content.find(r"{\fontsize{16}{20}\bfseries LIST OF TABLES\\[10pt]}")]
    new_lof = r"""{\fontsize{16}{20}\bfseries LIST OF FIGURES\\[10pt]}
\end{center}
\addcontentsline{toc}{section}{List of Figures}
\begin{longtable}{@{} c l c @{}}
\textbf{Figure No.} & \textbf{Figure Name} & \textbf{Page No.} \\[10pt]
1.1 & Domain Overview of ConvoShop & \pageref{fig:domain} \\[6pt]
3.1 & System Architecture Diagram & \pageref{fig:arch} \\[6pt]
4.1 & Flowchart of ConvoShop Pipeline & \pageref{fig:pipeline} \\[6pt]
4.2 & Context Fusion and LLM Reasoning & \pageref{fig:context} \\[6pt]
5.1 & Conversational Chat Interface & \pageref{fig:chat} \\[6pt]
5.2 & Product Recommendation Output & \pageref{fig:output} \\[6pt]
\end{longtable}

\newpage
\begin{center}
"""
    content = content.replace(old_lof, new_lof)
    
    # 6. Insert Images into the report
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
    content = content.replace(r"\subsection*{1.1 E-Commerce Background}", r"\subsection*{1.1 E-Commerce Background}" + fig_domain)

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
    content = content.replace(r"\subsection*{3.1 Hybrid RAG Architecture Overview}", r"\subsection*{3.1 Hybrid RAG Architecture Overview}" + fig_arch)

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
    content = content.replace(r"\subsection*{4.1 Data Cleaning and Normalization}", r"\subsection*{4.1 Data Cleaning and Normalization}" + fig_pipeline)

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
\caption{\textbf{Fig 4.2:} Context Fusion and LLM Reasoning. Merging query semantics with exact product metadata for zero-hallucination advisory.}
\label{fig:context}
\end{figure}
"""
    content = content.replace(r"\subsection*{4.3 The RAG Context Window}", r"\subsection*{4.3 The RAG Context Window}" + fig_context)

    # UI Images
    ui_chat_path = r"C:/Users/prana/.gemini/antigravity-ide/brain/d6b2f893-b0b0-4799-b27d-82987f7f0ac4/convo_chat_ui_1791630539838.png"
    ui_rec_path = r"C:/Users/prana/.gemini/antigravity-ide/brain/d6b2f893-b0b0-4799-b27d-82987f7f0ac4/convo_recommendation_ui_1791630551924.png"
    
    fig_chat = f"""
\\begin{{figure}}[h]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{ui_chat_path}}}
\\caption{{\\textbf{{Fig 5.1:}} Conversational Chat Interface. The primary frontend UI where users interact with the RAG agent.}}
\\label{{fig:chat}}
\\end{{figure}}
"""
    content = content.replace(r"\subsection*{5.1 Conversational Chat Interface}", r"\subsection*{5.1 Conversational Chat Interface}" + fig_chat)

    fig_output = f"""
\\begin{{figure}}[h]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{ui_rec_path}}}
\\caption{{\\textbf{{Fig 5.2:}} Product Recommendation Output. Dynamic product cards showcasing retrieved specs and AI rationale.}}
\\label{{fig:output}}
\\end{{figure}}
"""
    content = content.replace(r"\subsection*{5.2 Product Recommendation output}", r"\subsection*{5.2 Product Recommendation output}" + fig_output)


    # 7. Tables caption on top
    # Use regex to move \caption to the top of \begin{table}
    # Pattern: \begin{table}[h]\n\centering\n\begin{tabular} ... \end{tabular}\n\caption{...}\n\end{table}
    # We want \begin{table}[h]\n\centering\n\caption{...}\n\begin{tabular} ...
    tables = re.findall(r"(\\begin{table}.*?\\end{table})", content, flags=re.DOTALL)
    for table in tables:
        caption_match = re.search(r"(\\caption{.*?})", table)
        if caption_match:
            caption = caption_match.group(1)
            # Remove caption from bottom
            new_table = table.replace(caption, "")
            # Add caption above tabular
            new_table = new_table.replace(r"\begin{tabular}", caption + "\n" + r"\begin{tabular}")
            # Clean up double newlines
            new_table = new_table.replace("\n\n\\end{table}", "\n\\end{table}")
            content = content.replace(table, new_table)
            
    # Fix Table 5.1 formatting
    content = content.replace(r"\caption{Table 5.1: Quantitative Comparison", r"\caption{\textbf{Table 5.1:} Quantitative Comparison")

    # 8. Fix missing introductions between \subsection* and \subsubsection*
    # Find patterns like \subsection*{...}\n\subsubsection*{...}
    # And insert "This section explores the fundamental concepts and components regarding the topic discussed below."
    content = re.sub(r"(\\subsection\*\{.*?\})\n+(\\subsubsection\*\{.*?\})", 
                     r"\1\nThis section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.\n\n\2", 
                     content)
                     
    with open('c:/Users/prana/Desktop/tarun-project/Final_Report.tex', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_report()
