from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


class TopicModeling:

    def __init__(self, n_topics=5):

        self.n_topics = n_topics

        self.vectorizer = CountVectorizer(
            stop_words='english'
        )

        self.lda = LatentDirichletAllocation(
            n_components=n_topics,
            random_state=42
        )

    def fit(self, texts):

        X = self.vectorizer.fit_transform(texts)

        self.lda.fit(X)

    def get_topics(self, num_words=5):

        feature_names = self.vectorizer.get_feature_names_out()

        topics = []

        for topic_idx, topic in enumerate(self.lda.components_):

            words = [
                feature_names[i]
                for i in topic.argsort()[:-num_words - 1:-1]
            ]

            topics.append({
                "topic_id": topic_idx + 1,
                "keywords": words
            })

        return topics


if __name__ == "__main__":

    texts = [
        "Students lack career guidance",
        "Traffic congestion causes delays",
        "Social media addiction increasing",
        "Healthcare waiting time is high",
        "Online scams are growing"
    ]

    model = TopicModeling()

    model.fit(texts)

    print(model.get_topics())