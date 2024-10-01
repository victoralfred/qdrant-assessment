---
title: Database Optimization
weight: 2
---

# Frequently Asked Questions: Vector Search

### Would the order and combination of search terms affect the outcome of a vector search?
    e.g Will searching for "apples" and then filtering by "pears" yield the same results as searching for "apples pears" initially using a vector search?

Vectors capture the [semantic relationships](https://en.wikipedia.org/wiki/Semantic_search#:~:text=understanding%20the%20searcher%27s%20intent%20and%20the%20contextual%20meaning) between elements, enabling effective processing by LLM, the results you get for the queries "apples" and then filtered by "pears" versus directly searching for "apples pears" will likely not be the same. Here's why:
- Separate Queries ("apples" then filtered by "pears").
    -  ("apples"): The vector search would retrieve results related to "apples," providing documents, phrases, or passages that are semantically closest to the concept of apples.
    - Second query ("pears") as a filter: If you later filter these results by "pears," you’re essentially narrowing the results further to entries that are also relevant to "pears." This means the filtered results are documents that are related to both apples and pears, but the initial focus was on "apples."
- Combined Query ("apples pears")
    - In this case, the search is done for the combination of "apples" and "pears", and the vector search system will likely treat this as a single query, looking for documents that are semantically related to both terms from the start.
    - The vector representing "apples pears" will likely be quite different from either "apples" or "pears" individually, and the search results will reflect a more intertwined semantic understanding of these terms. The system might retrieve documents that talk about the relationship between apples and pears, or contexts where both are mentioned together.
- ###  Why Results Differ
    - <b>Contextual Interpretation:</b> Vector search models like those used in Qdrant or other semantic search engines capture the overall context and meaning of a query, not just the individual words. Searching for "apples" first focuses on that topic, while a combined query "apples pears" represents a more specific relationship between the two terms.
    - <b>Dimensional Difference:</b> In vector space, "apples" alone and "apples pears" combined will occupy different positions because the meaning changes when both terms are considered together. Adding "pears" as a second query after searching for "apples" alters the space you’re searching in differently than if both were used from the start.

If your goal is to find content that relates to both "apples" and "pears," it’s generally more efficient to search for "apples pears" together. If you need results more weighted towards "apples" but also want to consider "pears" later, then filtering after the fact is better.

### A brief overview of each search technique, their use cases, limitations, and when to use them
Qdrant, as a vector search engine, supports several search techniques that can be applied to different types of use cases. Each technique offers a unique approach to searching and retrieval, based on specific requirements for data exploration, context, and recommendations. Here’s a breakdown of the mentioned techniques along with their use cases, advantages, and limitations.

#### 1. Discovery Search
<b>Use Case</b>: Discovery search is used when you want to explore a dataset and find patterns, anomalies, or content that may not be immediately obvious. This technique is particularly useful for:
 - Data exploration: Uncovering new, previously unknown information or connections between entities.
 - Unsupervised learning: Grouping related documents, images, or entities based on their vector embeddings, often without any specific query.

##### Advantages:
- Helps in uncovering latent insights within datasets.
- Works well in situations where users don’t have a specific query but want to browse and explore a dataset.
##### Limitations:
- Results may be too broad or unfocused, especially if the user is looking for something specific.
- It may require significant human interpretation to make sense of the discovered patterns.
##### When to Use:
- When you don’t have a clear query but want to explore connections.
- During initial research or exploratory data analysis.

#### 2. Contextual Search
<b>Use case</b>: Contextual search leverages semantic relationships between terms or concepts. It goes beyond keyword matching by capturing the meaning and context of the search query, making it ideal for:
- <b>Natural language understanding</b>: Finding results based on the underlying meaning of a query rather than exact keywords.
- <b>Complex queries</b>: Handling long-form queries where the context matters (e.g., "What are the health benefits of apples in diets?").
- <b>Knowledge retrieval</b>: Retrieving documents or entities based on their relevance to the query’s context, not just word similarity.

##### Advantages:
-   Powerful in scenarios where keyword-based search fails due to the complexity or abstraction of the query.
- Can handle ambiguous or imprecise queries by understanding context and meaning.
- Useful for question-answering systems, chatbots, and semantic search engines.
##### Limitations:
- Heavily depends on the quality of the embeddings and the language model used to capture the context.
- May return unexpected results if the context is misunderstood by the system.
##### When to Use:
- When queries are natural language and require an understanding of meaning rather than direct matching.
- Useful in research, customer support, or any scenario where the context of the query plays a crucial role.

#### 3. Nearest Neighbor Search
<b>Use Case</b>: Nearest neighbor search is the core of most vector-based search engines, including Qdrant. It finds the closest vectors to the query vector based on a predefined distance metric (e.g., cosine similarity, Euclidean distance). Common use cases include:

- <b>Text or image search</b>: Finding the most similar documents, images, or entities.
Search by example: Users submit an example item, and the system retrieves similar items.
- <b>Anomaly detection</b>: Identifying items that are unusual or different based on their vector distance from the main cluster.
##### Advantages:
- Fast and efficient for high-dimensional data like text, images, and other embeddings.
- Direct and interpretable results based on the closest vector matches.
Works with a variety of distance metrics (Cosine, Euclidean, etc.).
##### Limitations:
- May return overly similar results, missing potentially relevant but more distant entities.
- Sensitive to the quality of the vector embeddings used—poor embeddings lead to poor results.
##### When to Use:
- When you have a clear query and want to find the most similar results.
- Ideal for content-based recommendations, similarity searches, and clustering tasks.
#### 4. Recommendation Search
**Use Case**: Recommendation systems aim to suggest content or entities that the user is likely to find relevant based on their past behavior or preferences. In the case of vector search, recommendations are generated by finding items that are similar in the vector space to the ones the user has interacted with. Use cases include:
- Product recommendations: Suggesting products based on past purchases or viewed items (e.g., recommending similar books, movies, or music).
- Content recommendation: Suggesting articles, blog posts, or documents based on previous reads.
- Personalization: Tailoring results to the specific preferences or behaviors of a user.
##### Advantages:
- Personalizes the search experience, increasing engagement and user satisfaction.
Works well with collaborative filtering and content-based filtering for diverse types of content.
- Scalable for large datasets, especially when using precomputed vectors for recommendations.
##### Limitations:
- Requires historical data about user preferences to make personalized recommendations.
- Can be limited in diversity, leading to filter bubbles (i.e., reinforcing the same type of content).
##### When to Use:
- When personalization is key, such as in e-commerce, media streaming, or news recommendation platforms.
- Ideal when user preferences can be inferred from prior interactions.

#### 5. Hybrid Search
**Use Case**: A combination of vector search and traditional keyword-based or metadata search, where you use both embeddings and structured data for more comprehensive searches. For example:
- E-commerce search: Use vector search to find similar products but filter by categories or price ranges using structured data.
- Multimodal search: Combining text and image vectors, or using vectors alongside metadata (like dates, tags, or categories).

##### Advantages:
- Leverages the strengths of both vector and traditional search techniques, allowing more precise results.
- Can handle complex queries that involve both semantic and structured data filtering.
##### Limitations:
- Adds complexity to query execution, as multiple techniques are involved.
- May require additional effort to fine-tune the balance between vector search and traditional filters.
##### When to Use:
- When the search query involves both semantic understanding and structured data filtering.
- Useful in complex search systems where users want both relevant and filtered results (e.g., product search by similarity but also by price range).

#### 6. Fuzzy Search
**Use Case**: Fuzzy search helps find results that are similar to, but not exact matches to, the query. It is useful in cases where:
- Misspellings: The user makes typographical errors in their query.
- Approximate matches: The query does not need to match the content exactly but should capture a general idea.

##### Advantages:
- More forgiving for user errors, improving the search experience.
- Helps find approximate matches, which can be useful in scenarios like user-generated content where spelling errors are common.
##### Limitations:
- May return less relevant results if the fuzziness threshold is too high.
Can slow down searches due to the need to consider a broader range of possible results.
##### When to Use:
- When user input is prone to errors or when exact matches are not critical.
