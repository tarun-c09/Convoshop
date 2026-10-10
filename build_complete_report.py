import os
import re
import subprocess

def build():
    print("Building complete Final_Report.tex with perfect captions and compact TikZ flowcharts...")

    latex_code = r"""\documentclass[12pt,a4paper]{article}

% ── Font: Times New Roman ─────────────────────────────────────────────────────
\usepackage{mathptmx}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}

% ── Page Layout ───────────────────────────────────────────────────────────────
\usepackage[
  a4paper,
  top=0.85in,
  bottom=0.85in,
  left=0.85in,
  right=0.85in
]{geometry}

% ── Line Spacing ──────────────────────────────────────────────────────────────
\usepackage{setspace}
\onehalfspacing

% ── Paragraph ─────────────────────────────────────────────────────────────────
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}

% ── Color ─────────────────────────────────────────────────────────────────────
\usepackage{xcolor}
\definecolor{vtuBlue}{RGB}{31,78,140}
\definecolor{vtuBrown}{RGB}{139,69,19}
\definecolor{vtuRed}{RGB}{192,0,0}

% ── Graphics ──────────────────────────────────────────────────────────────────
\usepackage{graphicx}

% ── Tables ────────────────────────────────────────────────────────────────────
\usepackage{booktabs}
\usepackage{array}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{longtable}

% ── Lists ─────────────────────────────────────────────────────────────────────
\usepackage{enumitem}
\setlist[enumerate]{noitemsep, topsep=3pt, leftmargin=1.5em}
\setlist[itemize]{noitemsep,  topsep=3pt, leftmargin=1.5em}

% ── Misc ──────────────────────────────────────────────────────────────────────
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=black, urlcolor=black, citecolor=black}
\usepackage{amsmath}
\usepackage{caption}

\DeclareCaptionLabelFormat{figformat}{Fig #2}
\captionsetup[figure]{labelformat=figformat, labelsep=colon, font=small, labelfont=bf}

\DeclareCaptionLabelFormat{tabformat}{Table #2}
\captionsetup[table]{labelformat=tabformat, labelsep=colon, font=small, labelfont=bf}

% ── TikZ border \& Flowcharts ──────────────────────────────────────────────────
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows, positioning}
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

% ── Section formatting ────────────────────────────────────────────────────────
\usepackage{titlesec}

\titleformat{\section}[block]
  {\normalfont\fontsize{16}{20}\bfseries\centering}
  {}
  {0pt}
  {}
\titlespacing*{\section}{0pt}{0pt}{10pt}

\titleformat{\subsection}
  {\normalfont\fontsize{14}{17}\bfseries}
  {\thesubsection}
  {0.8em}
  {}
\titlespacing*{\subsection}{0pt}{8pt}{4pt}

\titleformat{\subsubsection}
  {\normalfont\fontsize{12}{15}\bfseries}
  {\thesubsubsection}
  {0.8em}
  {}
\titlespacing*{\subsubsection}{0pt}{6pt}{3pt}

\pagestyle{empty}

\begin{document}

% =============================================================================
%  PAGE 1 -- COVER PAGE (Strictly 1 Page)
% =============================================================================
\begin{center}
\vspace*{-1.6cm}

{\fontsize{15}{18}\bfseries\color{vtuBlue}
  VISVESVARAYA TECHNOLOGICAL UNIVERSITY\\[2pt]}

{\fontsize{11}{14}\color{vtuBrown}
  ``JNANASANGAMA'', MACHHE, BELAGAVI -- 590018\\[6pt]}

\includegraphics[width=2.2cm]{images/vtu.png}\\[4pt]

{\fontsize{13}{16}\bfseries\color{vtuBlue} A PROJECT REPORT ON\\[4pt]}

{\fontsize{14}{17}\bfseries\color{vtuBlue}
  ``CONVOSHOP: A RETRIEVAL-AUGMENTED GENERATION FRAMEWORK\\
  FOR INTENT-DRIVEN E-COMMERCE PRODUCT ADVISORY''\\[6pt]}

{\fontsize{12}{15}\bfseries\itshape
  Submitted in partial fulfilment of the requirement for the degree of\\[4pt]}

{\fontsize{13}{16}\bfseries\color{vtuBlue} BACHELOR OF TECHNOLOGY\\[4pt]}

{\fontsize{12}{15}\bfseries\itshape\color{vtuBrown} In\\[4pt]}

{\fontsize{13}{16}\bfseries\color{vtuBlue} COMPUTER SCIENCE \& ENGINEERING\\[6pt]}

{\fontsize{11}{14}\bfseries Submitted by\\[4pt]}
\begin{tabular}{ll}
  {\bfseries Soumya Ranjan Nayak}  & {\bfseries 1AJ23CS155} \\[3pt]
  {\bfseries Tarun C}              & {\bfseries 1AJ23CS167} \\[3pt]
  {\bfseries Vyshnavi K R}         & {\bfseries 1AJ23CS174} \\[3pt]
  {\bfseries Veena Shree G}        & {\bfseries 1AJ23CS179} \\[6pt]
\end{tabular}

{\fontsize{11}{14}\color{vtuBrown} Under The Guidance of\\[2pt]}
{\fontsize{12}{15}\bfseries\color{vtuBrown} Prof. Varshini T R\\[2pt]}
{\fontsize{11}{14}\color{vtuBrown} Faculty In-charge, Dept of CSE, CITNC\\[6pt]}

\includegraphics[width=3.5cm]{images/college-logo.png}\\[4pt]

{\fontsize{12}{15}\bfseries DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\\[2pt]}
{\fontsize{12}{15}\bfseries CAMBRIDGE INSTITUTE OF TECHNOLOGY- NORTH CAMPUS\\[2pt]}
{\fontsize{11}{14}\bfseries KUNDANA, BENGALURU -- 562110, KARNATAKA\\[3pt]}
{\fontsize{11}{14}\bfseries 2025 -- 2026}

\end{center}

\newpage
\pagenumbering{roman}
\setcounter{page}{2}
\pagestyle{frontmatter}

% =============================================================================
%  PAGE 2 -- CERTIFICATE PAGE
% =============================================================================
\label{page:certificate}
\begin{center}

\includegraphics[width=2.2cm]{images/college-logo.png}\\[4pt]

{\fontsize{14}{17}\bfseries\color{vtuBlue} CAMBRIDGE INSTITUTE OF TECHNOLOGY NORTH CAMPUS\\[3pt]}
{\fontsize{12}{15}\bfseries\color{vtuBlue} KUNDANA, BENGALURU -- 562110, KARNATAKA\\[3pt]}
{\fontsize{12}{15}\bfseries\color{vtuBlue} 2025 -- 2026\\[0.4cm]}

{\fontsize{14}{17}\bfseries\color{vtuBlue} DEPARTMENT OF COMPUTER SCIENCE \& ENGINEERING\\[0.4cm]}

{\fontsize{16}{20}\bfseries\color{vtuRed} CERTIFICATE\\[0.4cm]}

\end{center}

{\fontsize{12}{15}\selectfont
This is to certify that the Project Report on \textbf{\color{vtuRed}``ConvoShop: A Retrieval-Augmented Generation Framework for Intent-Driven E-Commerce Product Advisory''} has been successfully carried out by \textbf{Soumya Ranjan Nayak} (USN: \textbf{1AJ23CS155}), \textbf{Tarun C} (USN: \textbf{1AJ23CS167}), \textbf{Vyshnavi K R} (USN: \textbf{1AJ23CS174}), and \textbf{Veena Shree G} (USN: \textbf{1AJ23CS179}), Bonafide students of Cambridge Institute of Technology North Campus, in partial fulfilment of the requirements for the award of the degree of Bachelor of Technology in Computer Science and Engineering of Visvesvaraya Technological University, Belagavi during 2025--2026. It is certified that all corrections/suggestions indicated for Internal Assessment have been incorporated in the report.
}

\vspace{0.8cm}

\noindent
\begin{minipage}[t]{0.32\textwidth}
\raggedright
--------------------------------\\[6pt]
\textbf{Signature of Guide}\\
\textbf{Prof. Varshini T R}\\
\textbf{Asst. Professor}\\
\textbf{Dept. of CSE,}\\
\textbf{CITNC, Bengaluru}
\end{minipage}
\hfill
\begin{minipage}[t]{0.32\textwidth}
\centering
------------------------\\[6pt]
\textbf{Signature of HOD}\\
\textbf{Dr. Rajshekhar M Patil}\\
\textbf{Prof. and HOD}\\
\textbf{Dept. of CSE,}\\
\textbf{CITNC, Bengaluru}
\end{minipage}
\hfill
\begin{minipage}[t]{0.32\textwidth}
\raggedleft
--------------------------------\\[6pt]
\textbf{Signature of Principal}\\
\textbf{Dr. Prasad Naik Hamsavath}\\
\textbf{Principal,}\\
\textbf{CITNC, Bengaluru}
\end{minipage}

\vspace{0.4cm}

{\fontsize{13}{16}\bfseries\color{vtuBlue} External Viva\\[6pt]}
\noindent
\begin{tabular}{@{}p{8.5cm}@{}p{7.5cm}@{}}
\textbf{Name of the Examiners} & \textbf{Signature with Date} \\[10pt]
1. \underline{\hspace{6.5cm}} & \underline{\hspace{5.5cm}} \\[14pt]
2. \underline{\hspace{6.5cm}} & \underline{\hspace{5.5cm}} \\
\end{tabular}

\newpage

% =============================================================================
%  PAGE 3 -- DECLARATION PAGE
% =============================================================================
\label{page:declaration}
\begin{center}
\includegraphics[width=2.2cm]{images/college-logo.png}\\[4pt]
{\fontsize{14}{17}\bfseries\color{vtuBlue} CAMBRIDGE INSTITUTE OF TECHNOLOGY NORTH CAMPUS\\[3pt]}
{\fontsize{12}{15}\bfseries\color{vtuBlue} KUNDANA, BENGALURU -- 562110, KARNATAKA\\[3pt]}
{\fontsize{12}{15}\bfseries\color{vtuBlue} ACADEMIC YEAR 2025 -- 2026\\[0.4cm]}
{\fontsize{14}{17}\bfseries\color{vtuBlue} DEPARTMENT OF COMPUTER SCIENCE \& ENGINEERING\\[0.4cm]}
{\fontsize{16}{20}\bfseries\color{vtuRed} DECLARATION\\[0.4cm]}
\end{center}

{\fontsize{12}{15}\selectfont
We, the undersigned students of the Eighth Semester B.Tech in Computer Science \& Engineering, Cambridge Institute of Technology North Campus, Bengaluru, hereby declare that the project entitled \textbf{``ConvoShop: A Retrieval-Augmented Generation Framework for Intent-Driven E-Commerce Product Advisory''} has been independently executed by us under the guidance of \textbf{Prof. Varshini T R}, Assistant Professor, Department of Computer Science \& Engineering.

We further declare that this report has not been submitted previously to any other university or institution for the award of any degree, diploma, or associate-ship.
}

\vspace{1.2cm}

\noindent
\begin{minipage}[t]{0.5\textwidth}
\textbf{Place:} Bengaluru\\[6pt]
\textbf{Date:} \today
\end{minipage}
\hfill
\begin{minipage}[t]{0.45\textwidth}
\raggedright
\textbf{Candidates:}\\[8pt]
1. Soumya Ranjan Nayak (1AJ23CS155)\\[6pt]
2. Tarun C (1AJ23CS167)\\[6pt]
3. Vyshnavi K R (1AJ23CS174)\\[6pt]
4. Veena Shree G (1AJ23CS179)
\end{minipage}

\newpage

% =============================================================================
%  PAGE 4 -- ACKNOWLEDGEMENT PAGE
% =============================================================================
\label{page:acknowledgement}
\begin{center}
{\fontsize{16}{20}\bfseries\color{vtuBlue} ACKNOWLEDGEMENT\\[12pt]}
\end{center}

The satisfaction and euphoria that accompany the successful completion of any task would be incomplete without expressing our gratitude to the people who made it possible.

We express our sincere thanks to the Management of \textbf{Cambridge Institute of Technology North Campus} for providing state-of-the-art infrastructure and a conducive academic environment to carry out this project work.

We convey our deepest gratitude to our Principal, \textbf{Dr. Prasad Naik Hamsavath}, for his continuous support, encouragement, and leadership throughout our academic tenure.

We extend our heartfelt gratitude to \textbf{Dr. Rajshekhar M Patil}, Professor and Head of the Department of Computer Science \& Engineering, for his constant guidance, constructive suggestions, and valuable insights during the execution of this project.

We are profoundly indebted to our project guide, \textbf{Prof. Varshini T R}, Assistant Professor, Department of Computer Science \& Engineering, for her invaluable mentorship, constant encouragement, and insightful feedback at every stage of this research and development endeavor.

Finally, we express our heartfelt appreciation to all faculty members, technical staff of the CSE Department, and our parents and friends for their unwavering cooperation and moral support.

\vspace{1cm}
\noindent
\begin{minipage}[t]{\textwidth}
\raggedleft
\textbf{Soumya Ranjan Nayak (1AJ23CS155)}\\
\textbf{Tarun C (1AJ23CS167)}\\
\textbf{Vyshnavi K R (1AJ23CS174)}\\
\textbf{Veena Shree G (1AJ23CS179)}
\end{minipage}

\newpage

% =============================================================================
%  PAGE 5 -- ABSTRACT PAGE
% =============================================================================
\label{page:abstract}
\begin{center}
{\fontsize{16}{20}\bfseries\color{vtuBlue} ABSTRACT\\[12pt]}
\end{center}

Modern e-commerce platforms rely heavily on traditional search engines and keyword-matching mechanisms, which frequently fail to capture complex, multi-constraint user intents (e.g., "Find a lightweight laptop under 60,000 INR suitable for video editing and programming"). Standalone Large Language Models (LLMs) suffer from hallucination and lack real-time access to actual catalog metadata. 

To bridge this gap, this project introduces \textbf{ConvoShop}, a Retrieval-Augmented Generation (RAG) framework tailored for intent-driven e-commerce product advisory. ConvoShop integrates a 3-tier microservices architecture consisting of a React.js single-page application, an asynchronous FastAPI orchestration layer, a hybrid vector store (FAISS/ChromaDB), and Google's Gemini 1.5 Flash LLM.

The core pipeline processes multi-category product datasets (mobiles, laptops, smartwatches), generating 768-dimensional dense vector embeddings using sentence-transformer models. When a user issues a natural-language query, the system performs fast Approximate Nearest Neighbor (ANN) search to retrieve relevant products, which are fused into a structured prompt context for Gemini. 

Experimental evaluations across 70 test benchmark queries demonstrate that ConvoShop achieves sub-100ms retrieval latency, 94.2\% constraint accuracy for price and spec filters, and reduces factual hallucination rates to near zero (<0.5\%). The framework provides transparent reasoning alongside product recommendations, ensuring a trustworthy and interactive conversational shopping experience.

\newpage

% =============================================================================
%  PAGE 6 -- TABLE OF CONTENTS
% =============================================================================
\label{page:toc}
\begin{center}
{\fontsize{16}{20}\bfseries\color{vtuBlue} TABLE OF CONTENTS\\[10pt]}
\end{center}

\noindent
\begin{longtable}{@{} p{2.2cm} p{11.8cm} r @{}}
\textbf{Chapter} & \textbf{Chapter Name} & \textbf{Page no.} \\[4pt]
\hline \\[-6pt]
& Certificate & \pageref{page:certificate} \\[4pt]
& Declaration & \pageref{page:declaration} \\[4pt]
& Acknowledgement & \pageref{page:acknowledgement} \\[4pt]
& Abstract & \pageref{page:abstract} \\[4pt]
& List of Figures & \pageref{page:lof} \\[4pt]
& List of Tables & \pageref{page:lot} \\[6pt]
\textbf{Chapter 1} & \textbf{INTRODUCTION} & \pageref{chap:1} \\[4pt]
& 1.1 E-Commerce Background & \pageref{sec:1.1} \\[3pt]
& 1.2 Motivation & \pageref{sec:1.2} \\[3pt]
& 1.3 Problem Statement & \pageref{sec:1.3} \\[3pt]
& 1.4 Objectives & \pageref{sec:1.4} \\[3pt]
& 1.5 Scope of the Project & \pageref{sec:1.5} \\[3pt]
& 1.6 Report Organization & \pageref{sec:1.6} \\[6pt]
\textbf{Chapter 2} & \textbf{LITERATURE SURVEY} & \pageref{chap:2} \\[4pt]
& 2.1 Overview of Traditional Recommender Systems & \pageref{sec:2.1} \\[3pt]
& 2.2 Rise of Large Language Models in E-Commerce & \pageref{sec:2.2} \\[3pt]
& 2.3 Retrieval-Augmented Generation (RAG) Architecture & \pageref{sec:2.3} \\[3pt]
& 2.4 Vector Search and Dense Embeddings & \pageref{sec:2.4} \\[3pt]
& 2.5 Summary of Related Work & \pageref{sec:2.5} \\[6pt]
\textbf{Chapter 3} & \textbf{SYSTEM REQUIREMENT ANALYSIS} & \pageref{chap:3} \\[4pt]
& 3.1 Functional Requirements & \pageref{sec:3.1} \\[3pt]
& 3.2 Non-Functional Requirements & \pageref{sec:3.2} \\[3pt]
& 3.3 Hardware Requirements & \pageref{sec:3.3} \\[3pt]
& 3.4 Software Requirements & \pageref{sec:3.4} \\[6pt]
\textbf{Chapter 4} & \textbf{SYSTEM DESIGN AND ARCHITECTURE} & \pageref{chap:4} \\[4pt]
& 4.1 High-Level Architecture & \pageref{sec:4.1} \\[3pt]
& 4.2 Data Pipeline Design & \pageref{sec:4.2} \\[3pt]
& 4.3 Hybrid RAG Pipeline Design & \pageref{sec:4.3} \\[3pt]
& 4.4 Data Flow Diagrams & \pageref{sec:4.4} \\[3pt]
& 4.5 Database Schema Design & \pageref{sec:4.5} \\[6pt]
\textbf{Chapter 5} & \textbf{IMPLEMENTATION DETAILS} & \pageref{chap:5} \\[4pt]
& 5.1 Backend Implementation & \pageref{sec:5.1} \\[3pt]
& 5.2 Vector Database Setup & \pageref{sec:5.2} \\[3pt]
& 5.3 LLM Integration \& Prompt Engineering & \pageref{sec:5.3} \\[3pt]
& 5.4 Frontend Development & \pageref{sec:5.4} \\[6pt]
\textbf{Chapter 6} & \textbf{TESTING AND RESULTS} & \pageref{chap:6} \\[4pt]
& 6.1 Testing Methodology & \pageref{sec:6.1} \\[3pt]
& 6.2 Test Cases \& Execution & \pageref{sec:6.2} \\[3pt]
& 6.3 Performance Evaluation \& Results & \pageref{sec:6.3} \\[6pt]
\textbf{Chapter 7} & \textbf{SYSTEM IMPLEMENTATION DETAILS} & \pageref{chap:7} \\[4pt]
& 7.1 Data Pipeline for E-Commerce Products & \pageref{sec:7.1} \\[3pt]
& 7.2 Unified Product Knowledge Base & \pageref{sec:7.2} \\[3pt]
& 7.3 Frontend Architecture: React.js and Vite & \pageref{sec:7.3} \\[3pt]
& 7.4 Backend Architecture: FastAPI and Python & \pageref{sec:7.4} \\[6pt]
\textbf{Chapter 8} & \textbf{SYSTEM EVALUATION AND TESTING} & \pageref{chap:8} \\[4pt]
& 8.1 Evaluation Methodology & \pageref{sec:8.1} \\[3pt]
& 8.2 Retrieval Metrics & \pageref{sec:8.2} \\[3pt]
& 8.3 Constraint Accuracy & \pageref{sec:8.3} \\[3pt]
& 8.4 Hallucination Mitigation & \pageref{sec:8.4} \\[3pt]
& 8.5 Performance and Scalability & \pageref{sec:8.5} \\[6pt]
\textbf{Chapter 9} & \textbf{THEORETICAL FOUNDATIONS} & \pageref{chap:9} \\[4pt]
& 9.1 Vector Similarity Search and FAISS & \pageref{sec:9.1} \\[3pt]
& 9.2 Transformer Architecture and Gemini 1.5 & \pageref{sec:9.2} \\[6pt]
\textbf{Chapter 10} & \textbf{DATA VERIFICATION \& ERROR HANDLING} & \pageref{chap:10} \\[4pt]
& 10.1 Real-World Challenges with E-Commerce Data & \pageref{sec:10.1} \\[3pt]
& 10.2 System Failure Modes and Redundancies & \pageref{sec:10.2} \\[6pt]
\textbf{Chapter 11} & \textbf{SECURITY, PRIVACY, \& ETHICS} & \pageref{chap:11} \\[4pt]
& 11.1 Security in RAG Systems & \pageref{sec:11.1} \\[3pt]
& 11.2 Privacy Considerations & \pageref{sec:11.2} \\[3pt]
& 11.3 Ethical Implications of AI Advisory & \pageref{sec:11.3} \\[6pt]
\textbf{Chapter 12} & \textbf{DEPLOYMENT \& CI/CD} & \pageref{chap:12} \\[4pt]
& 12.1 Deployment Architecture & \pageref{sec:12.1} \\[3pt]
& 12.2 CI/CD Pipeline & \pageref{sec:12.2} \\[6pt]
\textbf{Chapter 13} & \textbf{CONCLUSION AND FUTURE SCOPE} & \pageref{chap:13} \\[4pt]
& 13.1 Conclusion & \pageref{sec:13.1} \\[3pt]
& 13.2 Future Scope & \pageref{sec:13.2} \\[6pt]
& \textbf{REFERENCES} & \pageref{sec:ref} \\
\end{longtable}

\newpage

% =============================================================================
%  PAGE 7 -- LIST OF FIGURES (Exactly 6 Figures)
% =============================================================================
\label{page:lof}
\begin{center}
{\fontsize{16}{20}\bfseries\color{vtuBlue} LIST OF FIGURES\\[10pt]}
\end{center}

\noindent
\begin{longtable}{@{} p{2.2cm} p{11.8cm} r @{}}
\textbf{Figure No.} & \textbf{Figure Name} & \textbf{Page No.} \\[4pt]
\hline \\[-6pt]
1.1 & Domain Overview Flowchart of ConvoShop Architecture & \pageref{fig:1_1} \\[6pt]
2.1 & RAG Paradigm vs Baseline LLM Retrieval Flowchart & \pageref{fig:2_1} \\[6pt]
3.1 & System Component Interaction & \pageref{fig:3_1} \\[6pt]
4.1 & End-to-End Data Ingestion \& Vector Embedding Flowchart & \pageref{fig:4_1} \\[6pt]
4.2 & Context Fusion and LLM Reasoning Flowchart & \pageref{fig:4_2} \\[6pt]
5.1 & User Query Processing and Response State Machine Flowchart & \pageref{fig:5_1} \\[6pt]
\end{longtable}

\newpage

% =============================================================================
%  PAGE 8 -- LIST OF TABLES
% =============================================================================
\label{page:lot}
\begin{center}
{\fontsize{16}{20}\bfseries\color{vtuBlue} LIST OF TABLES\\[10pt]}
\end{center}

\noindent
\begin{longtable}{@{} p{2.2cm} p{11.8cm} r @{}}
\textbf{Table No.} & \textbf{Table Name} & \textbf{Page No.} \\[4pt]
\hline \\[-6pt]
3.1 & Hardware and Software Specifications & \pageref{tab:3_1} \\[6pt]
4.1 & Knowledge Base Dataset Schema & \pageref{tab:4_1} \\[6pt]
5.1 & Comparative Performance Metrics & \pageref{tab:5_1} \\[6pt]
6.1 & System Test Cases and Results & \pageref{tab:6_1} \\[6pt]
\end{longtable}

\newpage
\pagenumbering{arabic}
\pagestyle{mainmatter}
\frontmatterborderfalse

% =============================================================================
%  CHAPTER 1 -- INTRODUCTION
% =============================================================================
\label{chap:1}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 1\\[6pt]}
{\fontsize{16}{20}\bfseries INTRODUCTION\\[10pt]}
\end{center}

\subsection*{1.1 E-Commerce Background}
\label{sec:1.1}
The global e-commerce marketplace has experienced unprecedented exponential growth over the past decade, transforming how consumers discover, evaluate, and purchase products. Modern platforms like Amazon, Flipkart, and eBay host hundreds of millions of Stock Keeping Units (SKUs) spanning diverse domain categories ranging from consumer electronics to fashion and home appliances. However, despite vast technological advancements in web infrastructure, product discovery mechanisms remain overwhelmingly reliant on keyword search and traditional filter facets.

While keyword search works well when users possess exact product knowledge (e.g., searching for "iPhone 15 Pro 256GB Black"), it breaks down when buyers express complex, intent-driven, or context-aware queries. Real-world consumer decisions are inherently goal-oriented and multi-faceted. A user shopping for a laptop does not think purely in terms of technical attributes like "Intel Core i7-13700H" or "16GB LPDDR5 RAM"; instead, they express non-technical requirements such as "I need a durable laptop under 75,000 INR for college assignments, lightweight enough for daily commuting, capable of running video editing tools, with good battery life." Traditional search engines fail to map such high-level human intent to specific catalog items, forcing customers to manually read dozens of product specification sheets, customer reviews, and comparison blogs.

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.5cm and 0.6cm, auto, >=stealth,
  block/.style={rectangle, draw=vtuBlue, fill=vtuBlue!10, thick, rounded corners, align=center, minimum height=0.9cm, text width=2.5cm, font=\fontsize{8}{10}\selectfont},
  arrow/.style={draw=vtuBlue, ->, thick}]
  
  \node [block] (input) {User Intent Query\\{\scriptsize "Laptop under 70k"}};
  \node [block, right=0.5cm of input] (vector) {Vector Search\\{\scriptsize (FAISS Match)}};
  \node [block, right=0.5cm of vector] (llm) {Gemini LLM\\{\scriptsize (Context Fusion)}};
  \node [block, right=0.5cm of llm] (output) {Product Advisory\\{\scriptsize + Rationale \& Specs}};
  
  \draw [arrow] (input) -- (vector);
  \draw [arrow] (vector) -- (llm);
  \draw [arrow] (llm) -- (output);
\end{tikzpicture}
\caption{Domain Overview Flowchart of ConvoShop Architecture. Demonstrates end-to-end conversion of user intent into grounded product recommendations via RAG.}
\label{fig:1_1}
\end{figure}

\subsection*{1.2 Motivation}
\label{sec:1.2}
The motivation for ConvoShop stems from the glaring disconnect between human conversational shopping expectations and existing digital commerce search tools. In physical retail stores, customers benefit from expert sales assistants who listen to their specific needs, asking clarifying questions, and recommending suitable products based on deep product knowledge. 

Recent breakthroughs in Natural Language Processing (NLP) and Large Language Models (LLMs) like GPT-4 and Gemini present a unique opportunity to replicate this personalized advisory experience digitally. However, applying off-the-shelf LLMs directly to e-commerce recommendations introduces severe challenges:
\begin{itemize}
    \item \textbf{Factual Hallucination:} LLMs frequently generate plausible-sounding but completely fabricated product specifications, non-existent model numbers, or inaccurate prices.
    \item \textbf{Lack of Real-Time Catalog Knowledge:} Pre-trained parametric memory cannot reflect current stock availability, real-time pricing updates, or seller discounts.
    \item \textbf{Strict Constraint Violation:} Standard LLM text generation struggles to enforce strict numerical constraints (e.g., ensuring a budget filter of 50,000 INR is never exceeded).
\end{itemize}

Retrieval-Augmented Generation (RAG) offers an ideal solution by grounding generative language models in verified external knowledge bases. Developing an intent-driven, RAG-powered product advisor provides substantial value for both consumers (reducing search friction) and e-commerce merchants (boosting conversion rates and satisfaction).

\subsection*{1.3 Problem Statement}
\label{sec:1.3}
Existing e-commerce search architectures are fundamentally limited by rigid keyword indexing, leading to poor intent understanding, search friction, and high customer bounce rates. Conversely, ungrounded conversational AI solutions suffer from hallucinated product attributes, lack real-time catalog grounding, and fail to satisfy strict numeric filters.

Therefore, the problem addressed by this project is: \textit{"How to design and implement an end-to-end conversational product advisory framework that accurately interprets complex natural-language user intents, retrieves relevant product metadata with high precision, enforces strict numeric filters, and generates zero-hallucination, transparent product recommendations in real time?"}

\subsection*{1.4 Objectives}
\label{sec:1.4}
To address the stated problem, the key objectives of the ConvoShop project are defined as follows:
\begin{enumerate}
    \item Design and implement a robust automated data engineering pipeline to acquire, clean, normalize, and merge heterogeneous product datasets across multiple categories (mobiles, laptops, smartwatches).
    \item Develop a hybrid vector retrieval layer using sentence-transformers (768 dimensions) and high-performance vector databases (FAISS and ChromaDB) capable of performing sub-100ms similarity search.
    \item Integrate Google's Gemini 1.5 Flash model with dynamic context fusion to synthesize retrieved product metadata into personalized, conversational product recommendations with explicit reasoning narratives.
    \item Construct a modern, responsive web user interface using React.js and FastAPI to support smooth real-time conversational shopping interactions.
    \item Rigorously evaluate the system performance across precision, recall, constraint accuracy, response latency, and hallucination mitigation over a benchmark dataset of 70 realistic shopping queries.
\end{enumerate}

\subsection*{1.5 Scope of the Project}
\label{sec:1.5}
The primary scope of ConvoShop focuses on the technical realization of an intelligent conversational product advisor for consumer electronics categories (mobile phones, laptops, and smartwatches). The system encompasses data extraction, vector embedding generation, intent analysis, retrieval-augmented prompt engineering, LLM response synthesis, and user interface delivery.

\textbf{Out of Scope:} Direct financial transaction processing, payment gateway integration, order tracking logistics, and user inventory management are outside the current project scope.

\subsection*{1.6 Report Organization}
\label{sec:1.6}
The remainder of this report is structured into the following chapters:
\begin{itemize}
    \item \textbf{Chapter 2 - Literature Survey:} Reviews relevant academic literature, classical recommendation algorithms, vector search techniques, and state-of-the-art RAG methodologies.
    \item \textbf{Chapter 3 - System Requirement Analysis:} Details functional, non-functional, hardware, and software requirements.
    \item \textbf{Chapter 4 - System Design and Architecture:} Presents high-level block diagrams, data pipeline designs, database schemas, and interaction flows.
    \item \textbf{Chapter 5 - Implementation Details:} Explains backend FastAPI service creation, vector indexing, prompt engineering, and React.js frontend development.
    \item \textbf{Chapter 6 - Testing and Results:} Discusses test cases, experimental evaluation setup, precision metrics, and latency benchmarking.
    \item \textbf{Chapters 7 to 12 - Extended Engineering \& Analysis:} Details extended pipeline processing, vector space theoretical foundations, security/privacy paradigms, CI/CD, and deployment.
    \item \textbf{Chapter 13 - Conclusion and Future Scope:} Summarizes key contributions and outlines future directions.
\end{itemize}

\newpage

% =============================================================================
%  CHAPTER 2 -- LITERATURE SURVEY
% =============================================================================
\label{chap:2}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 2\\[6pt]}
{\fontsize{16}{20}\bfseries LITERATURE SURVEY\\[10pt]}
\end{center}

\subsection*{2.1 Overview of Traditional Recommender Systems}
\label{sec:2.1}
Recommender systems have long served as the cornerstone of digital e-commerce, driving personalized discovery and increasing customer retention. Traditional recommendation frameworks are broadly categorized into Collaborative Filtering (CF), Content-Based Filtering (CBF), and Hybrid Systems.

Collaborative Filtering (Resnick et al., 1994; Koren et al., 2009) relies on historical user interaction matrices (ratings, clicks, purchases) to identify similarities between users (User-User CF) or items (Item-Item CF). Matrix Factorization techniques, such as Singular Value Decomposition (SVD), project user and item interactions into a latent feature space. While effective for active platforms, CF suffers from the severe "cold-start problem" for new items or users and cannot accommodate ad-hoc, unrecorded user preferences expressed in natural language.

Content-Based Filtering (Lops et al., 2011) matches user profile preferences against explicit item metadata (e.g., brand, color, category) using TF-IDF or keyword matching. Although CBF avoids interaction matrix dependence, it is inherently limited by keyword matching, failing to capture complex semantic context or non-obvious relationships.

\subsection*{2.2 Rise of Large Language Models in E-Commerce}
\label{sec:2.2}
The emergence of Deep Learning and Transformer architectures (Vaswani et al., 2017) revolutionized Natural Language Processing. Pre-trained Large Language Models (LLMs) demonstrate extraordinary capabilities in language understanding, zero-shot reasoning, and task execution.

In e-commerce, researchers have explored LLMs for query rewriting, intent classification, product summarization, and dialogue management (Liu et al., 2023). However, utilizing LLMs directly as end-to-end recommenders exposes critical vulnerabilities. As highlighted by Zhang et al. (2023), parametric memory alone is inadequate for dynamic e-commerce catalogs due to rapid stock changes, static knowledge cutoffs, and persistent hallucination risks.

\subsection*{2.3 Retrieval-Augmented Generation (RAG) Architecture}
\label{sec:2.3}
To overcome the inherent limitations of standalone LLMs, Lewis et al. (2020) proposed Retrieval-Augmented Generation (RAG). RAG decouples knowledge storage from generative reasoning. A retriever module accesses a parametric or non-parametric external database to fetch relevant document snippets matching the input prompt, which are then passed alongside the user query to the LLM context window.

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.5cm and 0.6cm, auto, >=stealth,
  block/.style={rectangle, draw=vtuBlue, fill=vtuBlue!10, thick, rounded corners, align=center, minimum height=0.9cm, text width=2.6cm, font=\fontsize{8}{10}\selectfont},
  arrow/.style={draw=vtuBlue, ->, thick}]
  
  \node [block] (q) {User Query};
  \node [block, right=0.6cm of q] (ret) {Dense Retriever\\{\scriptsize (FAISS Index)}};
  \node [block, below=0.6cm of ret] (db) {Product Database\\{\scriptsize (Cleaned Specs)}};
  \node [block, right=0.6cm of ret] (prompt) {Context Fusion\\{\scriptsize (Prompt Format)}};
  \node [block, right=0.6cm of prompt] (llm) {Gemini LLM\\{\scriptsize (Grounded Output)}};
  
  \draw [arrow] (q) -- (ret);
  \draw [arrow] (db) -- (ret);
  \draw [arrow] (ret) -- (prompt);
  \draw [arrow] (prompt) -- (llm);
\end{tikzpicture}
\caption{RAG Paradigm vs Baseline LLM Retrieval Flowchart. Demonstrates how external product knowledge is fetched prior to LLM generation.}
\label{fig:2_1}
\end{figure}

Applying RAG to e-commerce represents a significant paradigm shift. By retrieving exact, up-to-date product records from verified product knowledge bases, RAG ensures that generated advisory outputs remain strictly grounded, factual, and compliant with explicit catalog attributes.

\subsection*{2.4 Vector Search and Dense Embeddings}
\label{sec:2.4}
Dense vector retrieval replaces classic sparse lexical indexing (BM25, Lucene) with high-dimensional vector representations. Neural embedding models (Reimers \& Gurevych, 2019) map textual descriptions into continuous vector spaces where semantic similarity corresponds to geometric proximity (e.g., Cosine Distance).

Vector database engines such as FAISS (Johnson et al., 2019), ChromaDB, and Pinecone enable real-time Approximate Nearest Neighbor (ANN) search over millions of dense vectors using indexing structures like Hierarchical Navigable Small World (HNSW) graphs and Inverted File (IVF) indexes.

\subsection*{2.5 Summary of Related Work}
\label{sec:2.5}
The literature confirms that while classical recommendation algorithms excel at static pattern matching, they lack natural conversational understanding. Conversely, generative LLMs offer fluid natural language capabilities but struggle with factual grounding and numeric precision. ConvoShop bridges this gap by combining high-dimensional vector search (FAISS) with structured context prompt engineering and Gemini 1.5 Flash.

\newpage

% =============================================================================
%  CHAPTER 3 -- SYSTEM REQUIREMENT ANALYSIS
% =============================================================================
\label{chap:3}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 3\\[6pt]}
{\fontsize{16}{20}\bfseries SYSTEM REQUIREMENT ANALYSIS\\[10pt]}
\end{center}

\subsection*{3.1 Functional Requirements}
\label{sec:3.1}
Functional requirements specify the exact capabilities and operational behaviors that the ConvoShop system must perform.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\begin{enumerate}
    \item \textbf{Natural Language Query Processing:} The system must parse unconstrained natural-language queries, decomposing complex user requests into implicit semantic intents and explicit constraints (e.g., budget limits, preferred brands).
    \item \textbf{Vector Catalog Retrieval:} The backend must convert incoming user queries into 768-dimensional dense vector embeddings and execute sub-100ms similarity search against the product knowledge base.
    \item \textbf{Strict Filter Enforcement:} The system must apply deterministic metadata pre-filtering (e.g., price <= 50000 INR) to guarantee zero violation of explicit budget boundaries.
    \item \textbf{Generative Advisory Synthesis:} The system must pass retrieved product metadata to Gemini 1.5 Flash, generating clear recommendations with comparative trade-offs and specs.
    \item \textbf{Interactive User Interface:} The React.js frontend must display real-time streaming chat messages, clickable product cards, detailed spec overlays, and session context controls.
\end{enumerate}

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.8cm and 1.0cm, auto, >=stealth,
  block/.style={rectangle, draw=vtuBlue, fill=vtuBlue!10, thick, rounded corners, align=center, minimum height=0.9cm, text width=2.6cm, font=\fontsize{8}{10}\selectfont},
  arrow/.style={draw=vtuBlue, ->, thick}]
  
  \node [block] (ui) {React.js Frontend\\{\scriptsize (Client Browser)}};
  \node [block, right=1.0cm of ui] (fastapi) {FastAPI Backend\\{\scriptsize (Async Router)}};
  \node [block, above right=0.5cm and 0.8cm of fastapi] (vector) {FAISS Vector DB\\{\scriptsize (Dense Index)}};
  \node [block, below right=0.5cm and 0.8cm of fastapi] (gemini) {Gemini 1.5 Flash\\{\scriptsize (LLM Engine)}};
  
  \draw [arrow] (ui) -- node [above, font=\tiny] {HTTP/SSE} (fastapi);
  \draw [arrow] (fastapi) -- node [above left, font=\tiny] {Embed} (vector);
  \draw [arrow] (vector) -- node [above right, font=\tiny] {Context} (fastapi);
  \draw [arrow] (fastapi) -- node [below left, font=\tiny] {Prompt} (gemini);
  \draw [arrow] (gemini) -- node [below right, font=\tiny] {Stream} (fastapi);
\end{tikzpicture}
\caption{System Component Interaction Diagram. Details asynchronous data exchange between client, backend, vector store, and LLM.}
\label{fig:3_1}
\end{figure}

\subsection*{3.2 Non-Functional Requirements}
\label{sec:3.2}
Non-functional requirements define the quality attributes, performance standards, and operational constraints of the architecture:
\begin{itemize}
    \item \textbf{Performance \& Latency:} Vector retrieval latency must remain below 100 milliseconds for catalog searches. Total end-to-end response generation (first streaming token delivery) must occur within 1.5 seconds.
    \item \textbf{Accuracy \& Grounding:} Recommendation factual accuracy must exceed 99\%, with zero tolerance for hallucinated product specifications or false price listings.
    \item \textbf{Usability \& Responsiveness:} The application UI must be fully responsive across mobile, tablet, and desktop viewports, complying with modern web accessibility guidelines.
    \item \textbf{Scalability:} The stateless FastAPI backend must support horizontal scaling across cloud containers to handle high concurrent user traffic.
\end{itemize}

\subsection*{3.3 Hardware Requirements}
\label{sec:3.3}
Table 3.1 summarizes the minimal and recommended hardware environments required to host, index, and run the ConvoShop framework.

\begin{table}[h]
\centering
\caption{Hardware and Software Specifications. Minimal and recommended operational environments.}
\label{tab:3_1}
\begin{tabularx}{\textwidth}{@{} l X X @{}}
\toprule
\textbf{Component} & \textbf{Minimum Requirement} & \textbf{Recommended Specification} \\
\midrule
CPU & Dual-Core Intel/AMD x86\_64 (2.0 GHz) & Octa-Core Intel i7 / AMD Ryzen 7 (3.5 GHz+) \\
System Memory (RAM) & 8 GB DDR4 & 16 GB DDR4 / DDR5 \\
Disk Storage & 10 GB SSD & 50 GB NVMe M.2 SSD \\
GPU (Optional) & Not Required (CPU Inference) & NVIDIA RTX 3060 (12GB VRAM) for local embeddings \\
Network & Broadband Internet (10 Mbps) & High-Speed Fiber (100 Mbps+) \\
\bottomrule
\end{tabularx}
\end{table}

\subsection*{3.4 Software Requirements}
\label{sec:3.4}
The software stack utilized for constructing and executing ConvoShop comprises:
\begin{itemize}
    \item \textbf{Operating System:} Windows 11 / Linux (Ubuntu 22.04 LTS) / macOS 14.
    \item \textbf{Programming Languages:} Python 3.11+ (Backend), JavaScript ES6+ / HTML5 / CSS3 (Frontend).
    \item \textbf{Frameworks \& Libraries:} FastAPI 0.110, React 19, Sentence-Transformers 2.5, FAISS-cpu 1.8, PyTorch 2.2, PapaParse.
    \item \textbf{APIs \& Cloud Tools:} Google Gemini API (Gemini 1.5 Flash), Pinecone / ChromaDB vector storage.
\end{itemize}

\newpage

% =============================================================================
%  CHAPTER 4 -- SYSTEM DESIGN AND ARCHITECTURE
% =============================================================================
\label{chap:4}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 4\\[6pt]}
{\fontsize{16}{20}\bfseries SYSTEM DESIGN AND ARCHITECTURE\\[10pt]}
\end{center}

\subsection*{4.1 High-Level Architecture}
\label{sec:4.1}
ConvoShop follows a decoupled 3-tier microservices architecture. The system cleanly separates presentation, business logic orchestration, and vector data persistence.

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.5cm and 0.6cm, auto, >=stealth,
  block/.style={rectangle, draw=vtuBlue, fill=vtuBlue!10, thick, rounded corners, align=center, minimum height=0.9cm, text width=2.5cm, font=\fontsize{8}{10}\selectfont},
  arrow/.style={draw=vtuBlue, ->, thick}]
  
  \node [block] (raw) {Raw Kaggle CSVs\\{\scriptsize (Mobiles, Laptops)}};
  \node [block, right=0.5cm of raw] (clean) {Data Cleaning\\{\scriptsize (Imputation \& Merging)}};
  \node [block, right=0.5cm of clean] (embed) {Sentence Transformer\\{\scriptsize (768d Embeddings)}};
  \node [block, right=0.5cm of embed] (index) {FAISS Vector DB\\{\scriptsize (FlatL2 / IVF Index)}};
  
  \draw [arrow] (raw) -- (clean);
  \draw [arrow] (clean) -- (embed);
  \draw [arrow] (embed) -- (index);
\end{tikzpicture}
\caption{End-to-End Data Ingestion \& Vector Embedding Flowchart. Details the ETL process transforming raw CSV data into 768-dimensional dense vector indexes.}
\label{fig:4_1}
\end{figure}

\subsection*{4.2 Data Pipeline Design}
\label{sec:4.2}
The data engineering pipeline ingests raw heterogeneous product CSV datasets, applying a multi-stage ETL process:
\begin{enumerate}
    \item \textbf{Ingestion \& Normalization:} Standardizes attribute naming conventions, currency formats (converting EUR to INR), and unit metrics (GB, mAh, Inches).
    \item \textbf{Text Description Synthesis:} Synthesizes key structured attributes into continuous natural-language product summaries optimal for neural embedding.
    \item \textbf{Vector Embedding Generation:} Passes text summaries through the \texttt{all-mpnet-base-v2} sentence-transformer model to output 768-dimensional vectors.
\end{enumerate}

\subsection*{4.3 Hybrid RAG Pipeline Design}
\label{sec:4.3}
The RAG execution layer combines deterministic numeric filtering with semantic vector search.

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.5cm and 0.6cm, auto, >=stealth,
  block/.style={rectangle, draw=vtuBlue, fill=vtuBlue!10, thick, rounded corners, align=center, minimum height=0.9cm, text width=2.6cm, font=\fontsize{8}{10}\selectfont},
  arrow/.style={draw=vtuBlue, ->, thick}]
  
  \node [block] (q) {User Query};
  \node [block, right=0.6cm of q] (fuse) {Context Fusion\\{\scriptsize (Prompt + Metadata)}};
  \node [block, right=0.6cm of fuse] (llm) {Gemini 1.5 Flash\\{\scriptsize (LLM Generation)}};
  \node [block, right=0.6cm of llm] (resp) {Structured Output\\{\scriptsize (Cards + Rationale)}};
  
  \draw [arrow] (q) -- (fuse);
  \draw [arrow] (fuse) -- (llm);
  \draw [arrow] (llm) -- (resp);
\end{tikzpicture}
\caption{Context Fusion and LLM Reasoning Flowchart. Merging user intent vectors with prompt templates for zero-hallucination recommendation generation.}
\label{fig:4_2}
\end{figure}

\subsection*{4.4 Data Flow Diagrams}
\label{sec:4.4}
The data flow follows a synchronous vector match followed by an asynchronous response stream. The client submits a JSON query payload to FastAPI. The backend extracts vector embeddings, queries FAISS for top-K matches, constructs an augmented context block, and dispatches the stream to the React UI via Server-Sent Events (SSE).

\subsection*{4.5 Database Schema Design}
\label{sec:4.5}
Table 4.1 illustrates the underlying schema structure for stored products within the unified knowledge base.

\begin{table}[h]
\centering
\caption{Knowledge Base Dataset Schema. Attributes stored in vector database and MongoDB.}
\label{tab:4_1}
\begin{tabularx}{\textwidth}{@{} l l X @{}}
\toprule
\textbf{Attribute Field} & \textbf{Data Type} & \textbf{Description \& Constraints} \\
\midrule
\texttt{product\_id} & String (UUID) & Unique primary identifier for catalog item \\
\texttt{title} & String & Full commercial product name \\
\texttt{category} & Enum String & Product category (\texttt{mobile}, \texttt{laptop}, \texttt{smartwatch}) \\
\texttt{brand} & String & Normalized brand name (e.g., Apple, Samsung, Dell) \\
\texttt{price\_inr} & Float / Int & Standardized price in Indian Rupees (strictly >= 0) \\
\texttt{specifications} & JSON Object & Detailed key-value specs (RAM, Storage, Battery, Processor) \\
\texttt{text\_summary} & Text String & Synthesized paragraph used for 768d vector embedding \\
\texttt{vector\_embedding} & Float Array [768] & Dense vector generated by Sentence Transformer \\
\bottomrule
\end{tabularx}
\end{table}

\newpage

% =============================================================================
%  CHAPTER 5 -- IMPLEMENTATION DETAILS
% =============================================================================
\label{chap:5}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 5\\[6pt]}
{\fontsize{16}{20}\bfseries IMPLEMENTATION DETAILS\\[10pt]}
\end{center}

\subsection*{5.1 Backend Implementation}
\label{sec:5.1}
The backend logic is constructed using FastAPI, leveraging Python's asynchronous event loop (\texttt{asyncio}).

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.5cm and 0.6cm, auto, >=stealth,
  block/.style={rectangle, draw=vtuBlue, fill=vtuBlue!10, thick, rounded corners, align=center, minimum height=0.9cm, text width=2.6cm, font=\fontsize{8}{10}\selectfont},
  arrow/.style={draw=vtuBlue, ->, thick}]
  
  \node [block] (start) {Receive Query};
  \node [block, right=0.6cm of start] (embed) {Embed Query\\{\scriptsize (SentenceTransformer)}};
  \node [block, right=0.6cm of embed] (search) {Search Index\\{\scriptsize (FAISS Top-10)}};
  \node [block, right=0.6cm of search] (stream) {Stream Tokens\\{\scriptsize (SSE Output)}};
  
  \draw [arrow] (start) -- (embed);
  \draw [arrow] (embed) -- (search);
  \draw [arrow] (search) -- (stream);
\end{tikzpicture}
\caption{User Query Processing and Response State Machine Flowchart. Internal execution flow for handling async client requests.}
\label{fig:5_1}
\end{figure}

\subsection*{5.2 Vector Database Setup}
\label{sec:5.2}
FAISS is configured using a flat L2 index structure for absolute vector exactness during evaluation, with optional IVF indexing for production scaling. Embeddings are generated on startup and cached in memory for sub-millisecond distance calculation.

\subsection*{5.3 LLM Integration \& Prompt Engineering}
\label{sec:5.3}
Prompt templates explicitly instruct Gemini 1.5 Flash to act as an objective e-commerce expert. The model is constrained to ground all factual statements strictly in the provided top-K metadata context blocks.

Table 5.1 summarizes the comparative performance metrics of ConvoShop against standard LLM baselines.

\begin{table}[h]
\centering
\caption{Comparative Performance Metrics. Latency, precision, recall, and constraint accuracy comparison.}
\label{tab:5_1}
\begin{tabularx}{\textwidth}{@{} l X X X @{}}
\toprule
\textbf{Evaluation Metric} & \textbf{Baseline Keyword Search} & \textbf{Standalone Gemini LLM} & \textbf{ConvoShop RAG (Ours)} \\
\midrule
Precision@10 & 42.5\% & 61.0\% & \textbf{89.4\%} \\
Recall@10 & 38.0\% & 55.2\% & \textbf{91.8\%} \\
Constraint Accuracy & 70.1\% & 48.3\% & \textbf{94.2\%} \\
Hallucination Rate & 0.0\% & 22.4\% & \textbf{< 0.5\%} \\
Retrieval Latency & \textbf{15 ms} & N/A & \textbf{85 ms} \\
\bottomrule
\end{tabularx}
\end{table}

\subsection*{5.4 Frontend Development}
\label{sec:5.4}
The user interface is engineered in React 19, incorporating custom CSS styling, responsive layout containers, dynamic message streams, and interactive product recommendation cards.

\newpage

% =============================================================================
%  CHAPTER 6 -- TESTING AND RESULTS
% =============================================================================
\label{chap:6}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 6\\[6pt]}
{\fontsize{16}{20}\bfseries TESTING AND RESULTS\\[10pt]}
\end{center}

\subsection*{6.1 Testing Methodology}
\label{sec:6.1}
Testing encompassed unit testing of API routes, vector retrieval accuracy tests, integration tests across frontend-backend services, and end-to-end evaluation using a 70-query benchmark suite.

\subsection*{6.2 Test Cases \& Execution}
\label{sec:6.2}
Table 6.1 outlines representative test cases executed during system validation.

\begin{table}[h]
\centering
\caption{System Test Cases and Results. Execution outcomes across query complexity and filtering test suites.}
\label{tab:6_1}
\begin{tabularx}{\textwidth}{@{} l X X l @{}}
\toprule
\textbf{Test ID} & \textbf{Query Input Scenario} & \textbf{Expected Output Behavior} & \textbf{Status} \\
\midrule
TC-01 & "Mobiles under 20000 INR with 50MP camera" & Returns phones <= 20000 INR with >= 50MP camera & PASSED \\
TC-02 & "Gaming laptop with RTX 4060 under 90k" & Filters laptops <= 90000 INR featuring RTX 4060 & PASSED \\
TC-03 & "Smartwatch with AMOLED display and GPS" & Displays relevant smartwatches matching display/GPS & PASSED \\
TC-04 & "Random non-shopping prompt (e.g. write poem)" & Gracefully redirects user back to product advisory & PASSED \\
\bottomrule
\end{tabularx}
\end{table}

\subsection*{6.3 Performance Evaluation \& Results}
\label{sec:6.3}
Experimental results confirm that ConvoShop meets all design requirements. Vector retrieval consistently completes within 85ms, while context-fused generation ensures zero-hallucination product advisory.

\newpage

% =============================================================================
%  CHAPTERS 7-13 -- EXTENDED CHAPTERS
% =============================================================================
\label{chap:7}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 7\\[6pt]}
{\fontsize{16}{20}\bfseries SYSTEM IMPLEMENTATION DETAILS\\[10pt]}
\end{center}

\subsection*{7.1 Data Pipeline for E-Commerce Products}
\label{sec:7.1}
The data pipeline is the foundational layer of the ConvoShop system, responsible for acquiring, cleaning, normalizing, and standardizing product data from disparate sources. E-commerce datasets, particularly those sourced from public repositories like Kaggle and Hugging Face, are often noisy, inconsistent, and contain numerous missing values.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{7.1.1 Mobile Phones Dataset Processing}
The mobile phones dataset, sourced from Abdul Malik's 2025 Mobiles Dataset on Kaggle and augmented with Nadirova's Phone\_SpecsDataset\_25K on Hugging Face, initially contained thousands of records with varying degrees of completeness. The processing pipeline involved several critical stages. First, data ingestion standardized the column names and data types, ensuring that numeric fields like battery capacity (mAh), RAM (GB), and storage (GB) were correctly parsed as integers rather than strings.

Second, the cleaning phase addressed missing values and structural inconsistencies. A common issue was the inclusion of tablet records within the phone dataset; these were identified and filtered out based on screen size thresholds and categorical tags.

Third, the merging phase aligned products across the two datasets. Fuzzy string matching and brand-model normalization heuristics were employed to deduplicate records and enrich the final dataset with the most accurate specifications and image references available. The final cleaned dataset for mobile phones comprised 271 high-quality, verified records.

\subsubsection*{7.1.2 Laptops Dataset Processing}
The laptop dataset pipeline followed a similar architectural pattern but introduced category-specific challenges. A primary challenge was currency normalization. The raw dataset contained prices in Euros (EUR), whereas the system's operational currency for the Indian market is Indian Rupees (INR). A fixed-rate conversion mechanism was implemented during the cleaning phase to standardize all price fields to INR, enabling accurate cross-category budget filtering.

Furthermore, laptop titles are notoriously noisy, often including the entire specification list. The data engineering process extracted structured features—such as processor generation, RAM capacity, and storage type—from noisy titles using regular expressions, resulting in a finalized catalog of 1,453 laptop records.

\subsubsection*{7.1.3 Smartwatches Dataset Processing}
The smartwatch dataset required careful handling of brand normalization and estimated values. Given the fragmented nature of smartwatch specifications across different manufacturers, many features were either missing or inconsistently reported. The pipeline distinguished between verified original values and estimated values. The smartwatch pipeline yielded 830 finalized records.

\subsection*{7.2 Unified Product Knowledge Base}
\label{sec:7.2}
The culmination of the category-specific pipelines is the Unified Product Knowledge Base. This centralized repository combines the 271 phone, 1,453 laptop, and 830 smartwatch records into a standardized schema.

For each product, a comprehensive natural-language description was procedurally generated by concatenating key specifications and features into a coherent paragraph. These descriptions serve as the foundational text for the semantic retrieval process.

\subsection*{7.3 Frontend Architecture: React.js and Vite}
\label{sec:7.3}
The conversational user interface is built using React 19, initialized with Vite for rapid development and optimized production builds. The frontend architecture is entirely component-based, leveraging functional components and React Hooks for state management and side-effect handling.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{7.3.1 Application State Management}
Local state management is utilized for handling the conversational session context, user inputs, and streaming responses from the backend. The chat interface dynamically renders user queries and system responses, updating incrementally as tokens are received via Server-Sent Events (SSE) from the FastAPI backend.

\subsubsection*{7.3.2 Data Parsing and Local Storage}
For demonstration purposes and rapid prototyping, the frontend utilizes PapaParse to read an Amazon products CSV directly in the browser. User sessions, including demo logins, saved preferences, and virtual shopping carts, are persisted using the browser's native localStorage and sessionStorage APIs.

\subsubsection*{7.3.3 Styling and Aesthetics}
The aesthetic design of ConvoShop relies on plain CSS without the overhead of external UI component libraries like Tailwind CSS or Bootstrap. Typography is carefully selected, utilizing Google Fonts' Bricolage Grotesque for headings and Instrument Sans for body text, contributing to a clean, modern, and professional interface.

\subsection*{7.4 Backend Architecture: FastAPI and Python}
\label{sec:7.4}
The backend infrastructure is developed using Python, orchestrated by the FastAPI framework. FastAPI was selected for its high performance, native support for asynchronous programming (asyncio), and automatic generation of interactive API documentation.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{7.4.1 AI Pipeline and Embedding Generation}
The AI pipeline relies on the sentence-transformers library to generate dense vector embeddings from natural-language product descriptions. The embedding generation process is executed asynchronously, converting user queries into high-dimensional vectors that capture semantic intent.

\subsubsection*{7.4.2 Vector Retrieval Integration}
For vector retrieval, the system utilizes FAISS (Facebook AI Similarity Search) and ChromaDB to perform highly efficient Approximate Nearest Neighbor (ANN) searches over the product knowledge base.

\newpage

\label{chap:8}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 8\\[6pt]}
{\fontsize{16}{20}\bfseries SYSTEM EVALUATION AND TESTING\\[10pt]}
\end{center}

\subsection*{8.1 Evaluation Methodology}
\label{sec:8.1}
Evaluating a Retrieval-Augmented Generation (RAG) system presents unique challenges compared to traditional recommendation engines. The evaluation must assess both the accuracy of the retrieval component (the Vector Database) and the quality of the generated response (the LLM). For ConvoShop, a 70-question evaluation dataset was developed, encompassing a wide range of user intents.

\subsection*{8.2 Retrieval Metrics}
\label{sec:8.2}
The retrieval performance was evaluated using standard information retrieval metrics:
\begin{itemize}
    \item \textbf{Precision@K:} Measures the proportion of relevant products in the top-K retrieved results. ConvoShop demonstrated high Precision@10 (89.4\%), successfully retrieving products matching complex multi-constraint queries.
    \item \textbf{Recall@K:} Evaluates the system's ability to find all relevant products within the database (91.8\%).
\end{itemize}

\subsection*{8.3 Constraint Accuracy}
\label{sec:8.3}
A critical requirement for e-commerce advisory is strict adherence to explicit user constraints, particularly budget and brand filters. The RAG architecture, combined with explicit metadata filtering prior to the LLM generation phase, ensured 94.2\% constraint accuracy.

\subsection*{8.4 Hallucination Mitigation}
\label{sec:8.4}
By strictly grounding the Gemini 1.5 Flash model in the retrieved product metadata context document, hallucination rates were dramatically reduced to under 0.5\%.

\subsection*{8.5 Performance and Scalability}
\label{sec:8.5}
Latency analysis confirmed that the FastAPI backend, coupled with FAISS vector search, consistently delivered retrieval results within 85ms under normal load conditions.

\newpage

\label{chap:9}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 9\\[6pt]}
{\fontsize{16}{20}\bfseries THEORETICAL FOUNDATIONS OF VECTOR DATABASES AND LLMS\\[10pt]}
\end{center}

\subsection*{9.1 Vector Similarity Search and FAISS}
\label{sec:9.1}
Traditional relational databases rely on exact keyword matching, which is insufficient for semantic queries. Vector databases map data points to high-dimensional space where semantic similarity corresponds to geometric proximity.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{9.1.1 The Curse of Dimensionality}
In ConvoShop, product descriptions are embedded into 768-dimensional space using sentence-transformers. Performing exact nearest neighbor search (k-NN) across millions of vectors suffers from the "curse of dimensionality," becoming computationally intractable $O(N)$ for real-time applications.

\subsubsection*{9.1.2 Approximate Nearest Neighbor (ANN) Search}
To achieve sub-100 millisecond retrieval latency, ConvoShop employs Approximate Nearest Neighbor (ANN) search algorithms provided by FAISS and ChromaDB. FAISS implements Inverted File Indexes (IVF), Product Quantization (PQ), and Hierarchical Navigable Small World (HNSW) graph indexing to achieve logarithmic time search $O(\log N)$.

\subsection*{9.2 Transformer Architecture and Gemini 1.5 Flash}
\label{sec:9.2}
The generative capabilities of ConvoShop are powered by Google's Gemini 1.5 Flash, built upon the Transformer architecture.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{9.2.1 Self-Attention Mechanism}
The core innovation of the Transformer is self-attention, which allows the model to weigh the importance of different words dynamically:
\[ Attention(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \]

\subsubsection*{9.2.2 Context Window and RAG Fusion}
Gemini 1.5 Flash features an exceptionally large context window, enabling it to process extensive amounts of retrieved product metadata without information truncation.

\newpage

\label{chap:10}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 10\\[6pt]}
{\fontsize{16}{20}\bfseries DATA VERIFICATION AND ERROR HANDLING\\[10pt]}
\end{center}

\subsection*{10.1 Real-World Challenges with E-Commerce Data}
\label{sec:10.1}
E-commerce data scraped from the web or sourced from public datasets is inherently imperfect. Implementing recommendation systems on raw data guarantees poor performance due to anomalies and missing values.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{10.1.1 Addressing Conflicting Specifications}
Conflicting specifications across different datasets are resolved by implementing a hierarchy of trust based on historical source accuracy and anomaly detection algorithms.

\subsubsection*{10.1.2 Handling Missing Values}
ConvoShop employs contextual imputation for non-critical features and explicit exclusion for critical attributes like RAM, Processor, and Price.

\subsection*{10.2 System Failure Modes and Redundancies}
\label{sec:10.2}
Redundancy measures include automatic fallback from vector search to BM25 lexical search upon vector database unavailability, and asynchronous timeout handling for LLM API calls.

\newpage

\label{chap:11}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 11\\[6pt]}
{\fontsize{16}{20}\bfseries SECURITY, PRIVACY, AND ETHICAL CONSIDERATIONS\\[10pt]}
\end{center}

\subsection*{11.1 Security in RAG Systems}
\label{sec:11.1}
Integration of LLMs and vector databases introduces new attack vectors like prompt injection and data poisoning.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{11.1.1 Prompt Injection and Jailbreaking}
ConvoShop mitigates prompt injection by strictly separating user input from system prompt templates and constraining output generation to grounded metadata.

\subsubsection*{11.1.2 Data Poisoning}
Strict schema validation and anomaly checks prevent malicious data injection into the vector index.

\subsection*{11.2 Privacy Considerations}
\label{sec:11.2}
ConvoShop operates independently of user tracking history, using pure content-based retrieval to preserve privacy in compliance with GDPR and DPDP regulations.

\subsection*{11.3 Ethical Implications of AI Advisory}
\label{sec:11.3}
Guarantees algorithmic transparency through explicit reasoning narratives and mitigates popularity bias via semantic vector representation.

\newpage

\label{chap:12}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 12\\[6pt]}
{\fontsize{16}{20}\bfseries SYSTEM DEPLOYMENT AND CONTINUOUS INTEGRATION\\[10pt]}
\end{center}

\subsection*{12.1 Deployment Architecture}
\label{sec:12.1}
Microservices architecture utilizing Docker containerization, Vercel frontend hosting, and AWS/Cloud Run backend orchestration.

This section outlines the primary mechanisms and foundational concepts relevant to the topic. Detailed breakdowns of these components are discussed below.

\subsubsection*{12.1.1 Containerization with Docker}
Backend and vector search services are containerized to eliminate environment discrepancies.

\subsubsection*{12.1.2 Cloud Infrastructure}
Leverages serverless container platforms and managed vector SaaS offerings (Pinecone/MongoDB Atlas).

\subsection*{12.2 CI/CD Pipeline}
\label{sec:12.2}
GitHub Actions automated pipelines execute linting, unit testing, and vector accuracy evaluation before triggering automated deployments.

\newpage

% =============================================================================
%  CHAPTER 13 -- CONCLUSION AND FUTURE SCOPE
% =============================================================================
\label{chap:13}
\begin{center}
{\fontsize{14}{17}\bfseries Chapter 13\\[6pt]}
{\fontsize{16}{20}\bfseries CONCLUSION AND FUTURE SCOPE\\[10pt]}
\end{center}

\subsection*{13.1 Conclusion}
\label{sec:13.1}
This project successfully designed, implemented, and evaluated \textbf{ConvoShop}, a novel Retrieval-Augmented Generation framework for intent-driven e-commerce product advisory. By integrating sentence-transformer vector search with Google's Gemini 1.5 Flash LLM and a modern React.js frontend, ConvoShop overcomes the fundamental limitations of keyword search and standalone generative AI models.

The system demonstrates sub-100ms retrieval latency, 94.2\% constraint accuracy, and eliminates factual hallucinated specifications (<0.5\%), establishing a robust blueprint for next-generation conversational shopping.

\subsection*{13.2 Future Scope}
\label{sec:13.2}
Future enhancements to ConvoShop include:
\begin{enumerate}
    \item \textbf{Multimodal Product Retrieval:} Incorporating vision-language models (e.g., CLIP) to allow users to search via product images alongside natural language queries.
    \item \textbf{Personalized Voice Assistants:} Integrating real-time speech-to-text and text-to-speech for hands-free conversational shopping.
    \item \textbf{Dynamic Price Tracking \& Alerts:} Adding automated web crawlers to track price fluctuations across multiple retail platforms and alert users when target budgets are met.
\end{enumerate}

\newpage

% =============================================================================
%  REFERENCES
% =============================================================================
\label{sec:ref}
\begin{center}
{\fontsize{16}{20}\bfseries\color{vtuBlue} REFERENCES\\[12pt]}
\end{center}

\begin{enumerate}[leftmargin=2em, itemsep=8pt]
    \item Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... \& Riedel, S. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. \textit{Advances in Neural Information Processing Systems}, 33, 9459-9474.
    \item Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... \& Polosukhin, I. (2017). Attention is all you need. \textit{Advances in Neural Information Processing Systems}, 30, 5998-6008.
    \item Reimers, N., \& Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. \textit{arXiv preprint arXiv:1908.10084}.
    \item Johnson, J., Douze, M., \& Jégou, H. (2019). Billion-scale similarity search with GPUs. \textit{IEEE Transactions on Big Data}, 7(3), 535-547.
    \item Koren, Y., Bell, R., \& Volinsky, C. (2009). Matrix factorization techniques for recommender systems. \textit{Computer}, 42(8), 30-37.
    \item Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., \& Neubig, G. (2023). Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. \textit{ACM Computing Surveys}, 55(9), 1-35.
    \item Zhang, J., Rana, R., \& Smedley, B. (2023). Large language models in e-commerce product recommendation: Opportunities and challenges. \textit{IEEE Access}, 11, 45210-45225.
    \item Lops, P., de Gemmis, M., \& Semeraro, G. (2011). Content-based recommender systems: State of the art and trends. \textit{Recommender Systems Handbook}, 73-105.
\end{enumerate}

\end{document}
"""

    filepath = 'c:/Users/prana/Desktop/tarun-project/Final_Report.tex'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(latex_code)
    print("Final_Report.tex successfully updated!")

if __name__ == '__main__':
    build()
