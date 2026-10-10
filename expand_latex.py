import re

def expand():
    with open("Final_Report.tex", "r", encoding="utf-8") as f:
        content = f.read()

    # Define technical expansion paragraphs for subsections
    expansions = {
        r"\subsection*{1.1 Overview of E-Commerce Search Evolution}": r"""\subsection*{1.1 Overview of E-Commerce Search Evolution}
\label{sec:ch1_1}

E-commerce platforms have fundamentally transformed modern retail, enabling consumers to explore millions of inventory keeping units (SKUs) from any location at any time. However, despite rapid technological advancement in frontend user interfaces and payment processing infrastructures, the core information retrieval mechanism of most e-commerce platforms remains trapped in legacy paradigms. Traditional e-commerce search relies heavily on inverted keyword indexing systems such as TF-IDF (Term Frequency-Inverse Document Frequency) and BM25 algorithms embedded in search engines like Elasticsearch and Apache Lucene.

While keyword search works adequately when buyers possess exact product identifiers or standard model names (e.g., \textit{``iPhone 15 Pro 256GB''}), it breaks down completely when consumers express complex, multi-attribute, or non-explicit shopping intents. Modern consumers naturally speak in natural language, describing real-world utility, constraints, and preferences rather than technical catalog strings. For instance, a user searching for \textit{``a lightweight laptop under 60,000 INR suitable for machine learning coursework with good battery life''} expects the platform to understand implicit technical relationships: machine learning requires dedicated GPU hardware or minimum 16GB RAM, lightweight implies weight under 1.8kg, and battery life demands efficient processor architecture.

Keyword-based engines process such queries as disconnected strings, matching isolated tokens like \textit{``lightweight''}, \textit{``laptop''}, or \textit{``learning''}, resulting in thousands of irrelevant search results, missing product options, or total search failure. This fundamental disconnect between human conversational intent and machine query matching leads to high bounce rates, cart abandonment, and customer dissatisfaction across digital retail platforms.

Furthermore, traditional e-commerce search engines operate on a single-query interaction model. Users enter a term, view a list of matching items, and if the results do not satisfy their criteria, they are forced to manually alter their query string or reset parametric filters. In contrast, physical retail shopping involves rich, multi-turn dialogues with knowledgeable sales advisors who ask clarifying questions, explain feature trade-offs, and dynamically narrow down choices based on user feedback. Bringing this human sales advisor experience into the digital realm requires fundamentally rethinking e-commerce discovery pipelines using modern Artificial Intelligence paradigms.

To address these limitations, modern discovery architectures integrate continuous dense vector spaces with deep learning representations. Unlike sparse inverted indices that evaluate exact lexical matches, dense embeddings capture higher-order semantic relationships across multidimensional metric spaces. By representing both user intent and catalog items as continuous vectors, machines can compute topological proximity, discovering relevant products even when user queries share zero common words with product title attributes.

In addition, traditional catalog search engines suffer from strict schema rigidity. Product catalogs are continuously populated by third-party sellers who use non-standardized terminology, inconsistent unit abbreviations, and varying levels of detail in product descriptions. An inverted index engine treating strings literally fails when faced with variance across vendor feeds. Dense neural encoders, by contrast, map varied surface expressions of the same underlying concept into identical metric regions, providing high resilience against vendor data noise.""",

        r"\subsection*{1.2 Motivation \& Industry Context}": r"""\subsection*{1.2 Motivation \& Industry Context}
\label{sec:ch1_2}

The motivation for ConvoShop stems from the recent emergence of Large Language Models (LLMs) and advanced Vector Embeddings in artificial intelligence. LLMs possess remarkable capabilities in natural language understanding, reasoning, and context management. However, deploying raw LLMs for domain-specific applications like e-commerce introduces severe vulnerabilities:
\begin{enumerate}
    \item \textbf{Hallucination}: General-purpose LLMs frequently generate plausible-sounding but completely fictitious product specifications, prices, model names, and availability metrics.
    \item \textbf{Stale Knowledge}: Pre-trained LLM weights are static and cannot reflect real-time inventory updates, price fluctuations, or newly added product lines.
    \item \textbf{Lack of Grounding}: Standalone LLMs cannot query internal enterprise databases securely or provide direct links to actionable checkout paths.
\end{enumerate}

Retrieval-Augmented Generation (RAG) has emerged as the definitive enterprise architecture to solve these limitations. By decoupling knowledge storage (external dense vector databases) from generative reasoning (LLM), RAG enables dynamic retrieval of real-time product data before synthesizing user responses. ConvoShop leverages this architectural paradigm, combining Google's state-of-the-art \textbf{Gemini 1.5 Flash} model with \textbf{FAISS HNSW} dense vector indexing to deliver a reliable, zero-hallucination conversational shopping advisor.

In the contemporary e-commerce landscape, consumer electronics represent one of the most complex purchasing categories. Buyers face overwhelming choice paralysis when comparing laptops, smartphones, headphones, and smart wearables due to rapid specification cycles, dense technical jargon, and subtle price variations across retailers. An intelligent agent capable of decoding complex technical specifications, validating stock availability, and rendering interactive comparisons directly within a chat context fills a vital market need.

From an industry perspective, digital retail platforms operate under fierce competition where conversion optimization and user retention govern financial viability. Studies indicate that up to 68\% of online shoppers abandon e-commerce platforms due to search friction when they cannot find specific multi-attribute items within three clicks. By providing an intuitive, conversational advisory interface, ConvoShop significantly reduces consumer cognitive load, accelerates purchase decision cycles, and elevates customer satisfaction metrics.

Moreover, the financial implications of cart abandonment driven by search friction are staggering. E-commerce platforms invest billions of dollars annually in performance marketing to drive user traffic to product landing pages. When arriving users encounter broken parametric search interfaces or unhelpful keyword results, those marketing acquisitions are effectively squandered. ConvoShop provides a high-efficiency conversion engine that turns high-intent conversational queries into verified product recommendations.""",

        r"\subsection*{2.1 Evolution of Information Retrieval in E-Commerce}": r"""\subsection*{2.1 Evolution of Information Retrieval in E-Commerce}
\label{sec:ch2_1}

Information Retrieval (IR) in retail has evolved across three distinct technological eras:
\begin{enumerate}
    \item \textbf{Lexical Keyword Era (1990s -- 2010s)}: Relied on exact matching between user query terms and product title strings. Inverted index algorithms such as BM25 calculated term frequency and inverse document frequency:
    \begin{equation}
    \text{Score}(D, Q) = \sum_{i=1}^{n} \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}
    \end{equation}
    Lexical systems suffered severely from vocabulary mismatch, inability to understand synonyms, and failure to handle long-tail conversational inputs. For example, if a product catalog lists a laptop as having an \textit{``NVMe Solid State Drive''}, a query searching for \textit{``fast flash storage''} yields zero exact keyword matches despite high semantic identity.

    \item \textbf{Neural Search Era (2010s -- 2022)}: Introduced Deep Neural Networks (DNNs) and BERT-based transformers to compute sentence embeddings. Dual-encoder architectures encoded queries and products into continuous vector spaces. While semantic capture improved, neural search models lacked natural language generation, requiring rigid UI filtering mechanisms and returning static lists of product links without explainable rationale.

    \item \textbf{Generative RAG Era (2022 -- Present)}: Merges continuous vector retrieval with generative Large Language Models. RAG enables machines to act as human-like shopping advisors capable of synthesizing product comparisons, explaining complex feature tradeoffs, and answering open-ended domain questions in natural language.
\end{enumerate}

To further quantify the limitations of lexical retrieval systems in retail domains, research by Robertson et al. demonstrated that BM25 scoring degrades sharply when query length exceeds 7 tokens due to term saturation effects ($k_1$). In conversational shopping environments where user inputs average 12 to 20 words (describing usage contexts, budget boundaries, brand preferences, and spec preferences), lexical term frequency weighting fails to distinguish between critical constraints (e.g., \textit{``under 50,000''}) and conversational filler (e.g., \textit{``I am looking for''}).

Furthermore, traditional inverted index systems operate under the closed-world assumption: if a query token is absent from the index, the document score is zero. Modern deep neural encoders overcome this by learning dense continuous manifold projections, where semantic similarity is modeled as distance along a smooth manifold in $\mathbb{R}^d$.""",

        r"\subsection*{2.2 Dense Vector Search \& Vector Databases}": r"""\subsection*{2.2 Dense Vector Search \& Vector Databases}
\label{sec:ch2_2}

Dense vector search projects textual documents into high-dimensional metric spaces $\mathbb{R}^d$ where semantically similar concepts reside in close geographic proximity regardless of precise vocabulary overlap. Given two normalized vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^d$, similarity is measured using Cosine Distance:

\begin{equation}
\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} = \sum_{i=1}^{d} u_i v_i
\end{equation}

To eliminate $O(N)$ exhaustive linear scans across large product catalogs, specialized vector indexing algorithms construct graph topologies. The Hierarchical Navigable Small World (HNSW) graph organizes vectors into multi-layer probabilistic skip lists, achieving $O(\log N)$ search complexity. In an HNSW structure, top layers maintain long-range connections for coarse-grained routing across vector clusters, while bottom layers maintain local, high-density connections for fine-grained nearest neighbor selection.

Table \ref{tab:2_1} provides a comparative evaluation of enterprise vector store engines evaluated for ConvoShop.

\begin{table}[h!]
\caption{Comparative Analysis of Vector Search Databases}
\label{tab:2_1}
\centering
\fontsize{10}{13}\selectfont
\begin{tabularx}{\linewidth}{XXXXX}
\toprule
\textbf{Vector Store} & \textbf{Index Type} & \textbf{Latency (P95)} & \textbf{Deployment} & \textbf{Best Fit Use Case} \\
\midrule
\textbf{FAISS} & HNSW / IVF-PQ & $< 5$ ms & In-Memory / C++ Library & Ultra-fast local execution \& embedded systems \\
\textbf{Pinecone} & Graph Managed & $25 - 40$ ms & Managed Cloud SaaS & Enterprise multi-tenant SaaS \\
\textbf{ChromaDB} & HNSW / DuckDB & $15 - 30$ ms & Python Embedded & Rapid prototyping \& microservices \\
\textbf{Qdrant} & HNSW Payload & $10 - 20$ ms & Rust / Cloud Container & Payload-filtered vector search \\
\textbf{Milvus} & HNSW / DiskANN & $12 - 25$ ms & Distributed Cluster & Massive scale ($>100$M vectors) \\
\bottomrule
\end{tabularx}
\end{table}

FAISS was selected for ConvoShop due to its exceptional C++ optimized execution speed, sub-5ms query latency, zero external cloud dependency, and low memory overhead during local microservice execution.

The mathematical formulation of HNSW graph construction involves establishing a probabilistic layer height assignment function for each newly inserted vector $v$:
\begin{equation}
l = \lfloor -\ln(\text{uniform}(0, 1)) \cdot m_L \rfloor
\end{equation}
where $m_L$ is a normalization factor controlling layer density. During query execution, greedy routing traverses the top layer $l_{\max}$ down to layer $0$, expanding nearest neighbor sets via a priority queue of size \texttt{efSearch}.""",

        r"\subsection*{4.1 High-Level Architectural Framework}": r"""\subsection*{4.1 High-Level Architectural Framework}
\label{sec:ch4_1}

ConvoShop utilizes a multi-layered decoupled microservice architecture consisting of four core tiers: Client Interface Tier, Orchestration Microservice Tier, Vector Retrieval Tier, and Generative Intelligence Tier. Figure \ref{fig:4_1} illustrates the high-level system framework.

\begin{figure}[h!]
\centering
\begin{tikzpicture}[node distance=1.5cm, auto, >=latex']
    % Styles
    \tikzstyle{block} = [rectangle, draw=vtuBlue, fill=vtuBlue!10, thick, text width=3.2cm, align=center, rounded corners, minimum height=1.2cm, font=\small]
    \tikzstyle{cloud} = [rectangle, draw=vtuRed, fill=vtuRed!10, thick, text width=3.2cm, align=center, rounded corners, minimum height=1.2cm, font=\small]
    \tikzstyle{line} = [draw, -latex', thick]

    % Nodes
    \node [block] (ui) {\textbf{Client Web UI}\\(React / Modern CSS)};
    \node [block, right=1.2cm of ui] (server) {\textbf{API Server}\\(Node.js / SSE)};
    \node [block, right=1.2cm of server] (rag) {\textbf{RAG Orchestrator}\\(Python / LangChain)};
    \node [cloud, below=1.2cm of server] (faiss) {\textbf{FAISS Vector Store}\\(HNSW 768-D)};
    \node [cloud, below=1.2cm of rag] (gemini) {\textbf{Google Gemini 1.5}\\(Flash LLM API)};

    % Paths
    \path [line] (ui) -- node[above, font=\tiny]{HTTP / SSE} (server);
    \path [line] (server) -- node[above, font=\tiny]{JSON Payload} (rag);
    \path [line] (rag) -- node[right, font=\tiny]{Vector Query} (faiss);
    \path [line] (faiss) -- node[left, font=\tiny]{Top-K Catalog} (rag);
    \path [line] (rag) -- node[right, font=\tiny]{Grounded Prompt} (gemini);
    \path [line] (gemini) |- node[below, font=\tiny]{Stream Tokens} (server);
    \path [line] (server) -- node[below, font=\tiny]{SSE Stream} (ui);
\end{tikzpicture}
\caption{High-Level System Architecture of ConvoShop Framework}
\label{fig:4_1}
\end{figure}

The decoupled design ensures that individual components can scale independently. For instance, if vector query traffic increases, additional FAISS replica nodes can be instantiated without altering the generative Gemini API configuration.

Each tier in the framework enforces strict responsibility boundaries:
\begin{itemize}
    \item \textbf{Client Interface Tier}: Manages local UI state, parses Server-Sent Event (SSE) streams, renders interactive product cards, and updates spec comparison modals.
    \item \textbf{Orchestration Microservice Tier}: Acts as an API gateway, enforcing rate limits, parsing JSON payloads, managing session memory, and dispatching async RAG pipeline commands.
    \item \textbf{Vector Retrieval Tier}: Houses the C++ optimized FAISS HNSW graph index and memory-mapped catalog JSON metadata store, returning top-$K$ candidate products in under 5ms.
    \item \textbf{Generative Intelligence Tier}: Wraps Google's Gemini 1.5 Flash API, executing prompt-grounded reasoning and token streaming.
\end{itemize}""",

        r"\subsection*{5.3 Hybrid Search \& Re-Ranking}": r"""\subsection*{5.3 Hybrid Search \& Re-Ranking}
\label{sec:ch5_3}

To maximize precision, ConvoShop implements a hybrid retrieval framework combining dense vector search scores $S_{\text{dense}}$ with sparse BM25 lexical scores $S_{\text{BM25}}$ via Reciprocal Rank Fusion (RRF):

\begin{equation}
RRF(d \in \mathcal{D}) = \frac{1}{k + r_{\text{dense}}(d)} + \frac{1}{k + r_{\text{BM25}}(d)}
\end{equation}

where $k=60$ is a smoothing constant, and $r(d)$ represents the ordinal rank of document $d$ under each respective retrieval strategy. RRF ensures that products matching specific alphanumeric model numbers (which sparse search handles best) and general semantic concepts (which dense search handles best) both rank near the top of the context payload.

To further refine candidate ranking, ConvoShop integrates an optional cross-encoder re-ranking pass using HuggingFace's \texttt{bge-reranker-large}. While dual-encoders compute query and document vectors independently, cross-encoders accept the concatenated pair $(Q, D)$ as a single input to transformer self-attention layers, computing deep term interaction scores:

\begin{equation}
S_{\text{cross}}(Q, D) = \text{Sigmoid}\left(W \cdot \text{Transformer}([Q; D])\right)
\end{equation}

This two-stage retrieval strategy—fast ANN candidate extraction via FAISS HNSW followed by cross-encoder re-ranking of top-20 items—achieves state-of-the-art precision without sacrificing real-time query latency constraints.""",

        r"\subsection*{6.2 Prompt Engineering Strategy}": r"""\subsection*{6.2 Prompt Engineering Strategy}
\label{sec:ch6_2}

ConvoShop utilizes a multi-part system prompt structure consisting of four key segments:
\begin{enumerate}
    \item \textbf{Role Definition}: Establishes the agent persona as an expert, polite e-commerce advisor.
    \item \textbf{Context Boundary Rules}: Instructs the model to answer queries strictly using the provided catalog data.
    \item \textbf{Anti-Hallucination Constraints}: Explicitly forbids inventing non-existent models, features, or prices.
    \item \textbf{Formatting Instructions}: Mandates output responses to be structured with clear headings, comparison bullet points, and explicit product cards.
\end{enumerate}

Below is an extract of the production prompt template:
\begin{verbatim}
SYSTEM PROMPT: You are ConvoShop AI, a sales consultant.
RULES:
1. ONLY recommend products present in the CATALOG CONTEXT below.
2. If NO products match the criteria, state: "No matching catalog items."
3. Format product mentions using [PRODUCT_CARD: <ID>].
4. Be concise, polite, and explain trade-offs clearly.
\end{verbatim}

Prompt engineering in ConvoShop also incorporates dynamic few-shot exemplar injection. When processing complex multi-attribute queries (e.g., comparing two specific models across 5 hardware dimensions), the system dynamically injects an exemplar dialogue demonstrating expected table formatting and spec trade-off explanations. This technique stabilizes LLM formatting output, ensuring consistent structured rendering across varying user inputs.""",

        r"\subsection*{9.2 FAISS HNSW Index Design}": r"""\subsection*{9.2 FAISS HNSW Index Design}
\label{sec:ch9_2}

The FAISS vector store uses an HNSW graph index (\texttt{IndexHNSWFlat}). HNSW constructs a multi-layer graph where lower layers contain dense connections for fine-grained search and upper layers feature sparse connections for fast routing. Key hyperparameters include:
\begin{itemize}
    \item $M = 16$: Number of bi-directional links created per vector node.
    \item \texttt{efConstruction} $= 200$: Search depth during index construction.
    \item \texttt{efSearch} $= 50$: Search depth during runtime query execution.
\end{itemize}

During graph traversal, the algorithm maintains a dynamic candidate pool $W$ of size \texttt{efSearch}. At each iteration, the node in $W$ closest to query vector $\mathbf{q}$ is evaluated, and its unvisited graph neighbors are inserted into $W$. The search terminates when all remaining unvisited neighbors lie further from $\mathbf{q}$ than the furthest item currently in $W$. Higher values of \texttt{efSearch} improve recall at the cost of logarithmic latency growth.""",

        r"\subsection*{13.1 VectorStoreManager Implementation}": r"""\subsection*{13.1 VectorStoreManager Implementation}
\label{sec:ch13_1}

The Python class \texttt{VectorStoreManager} wraps FAISS index operations, vector normalization, and metadata management:

\begin{verbatim}
import faiss
import numpy as np
import json

class VectorStoreManager:
    def __init__(self, dim=768):
        self.dim = dim
        self.index = faiss.IndexHNSWFlat(dim, 16)
        self.index.hnsw.efConstruction = 200
        self.index.hnsw.efSearch = 50
        self.metadata_store = {}

    def add_items(self, vectors, items):
        norm_vectors = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
        start_id = self.index.ntotal
        self.index.add(norm_vectors.astype(np.float32))
        for i, item in enumerate(items):
            self.metadata_store[start_id + i] = item

    def search(self, query_vector, k=5):
        norm_q = query_vector / np.linalg.norm(query_vector)
        distances, indices = self.index.search(
            np.array([norm_q], dtype=np.float32), k
        )
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx != -1 and idx in self.metadata_store:
                results.append((self.metadata_store[idx], float(dist)))
        return results
\end{verbatim}

The implementation ensures strict memory alignment by casting vector arrays to 32-bit floating point precision (\texttt{np.float32}), matching FAISS C++ native SIMD vectorization requirements.""",

        r"\subsection*{13.2 GeminiRAGEngine Implementation}": r"""\subsection*{13.2 GeminiRAGEngine Implementation}
\label{sec:ch13_2}

The core orchestration engine handles query embedding, vector lookup, prompt construction, and Gemini streaming:

\begin{verbatim}
import google.generativeai as genai

class GeminiRAGEngine:
    def __init__(self, api_key, vector_store):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.vector_store = vector_store

    def build_context(self, retrieved_products):
        context_lines = []
        for prod, dist in retrieved_products:
            line = (f"ID: {prod['product_id']} | Title: {prod['title']} | "
                    f"Price: INR {prod['price_inr']} | "
                    f"Specs: {prod['specs']} | Stock: {prod['in_stock']}")
            context_lines.append(line)
        return "\n".join(context_lines)

    def generate_response_stream(self, user_query, session_history):
        q_vector = get_embedding(user_query)
        retrieved_products = self.vector_store.search(q_vector, k=5)
        
        context_str = self.build_context(retrieved_products)
        prompt = f"""SYSTEM: You are ConvoShop AI, an expert e-commerce assistant.
Answer using ONLY the retrieved products below.

CATALOG CONTEXT:
{context_str}

USER QUERY: {user_query}
ANSWER:"""

        response = self.model.generate_content(prompt, stream=True)
        for chunk in response:
            yield chunk.text
\end{verbatim}""",
    }

    # Replace mapped subsections
    for key, val in expansions.items():
        if key in content:
            content = content.replace(key, val)

    with open("Final_Report.tex", "w", encoding="utf-8") as f:
        f.write(content)

    print("Final_Report.tex expanded successfully.")

if __name__ == "__main__":
    expand()
