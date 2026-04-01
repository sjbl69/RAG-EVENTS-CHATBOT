# Évaluation RAG 

def compute_context_precision(contexts, ground_truth):
    correct = 0
    total = len(contexts)

    for ctx_list, gt in zip(contexts, ground_truth):
        if any(gt.lower() in ctx.lower() for ctx in ctx_list):
            correct += 1

    return correct / total


def compute_context_recall(contexts, ground_truth):
    found = 0
    total = len(ground_truth)

    for ctx_list, gt in zip(contexts, ground_truth):
        if any(gt.lower() in ctx.lower() for ctx in ctx_list):
            found += 1

    return found / total


# Dataset d’évaluation

def build_eval_dataset():
    return {
        "question": [
            "Quels événements culturels à Lyon ce week-end ?",
            "Y a-t-il des expositions gratuites ?"
        ],
        "contexts": [
            [
                "Festival de musique à Lyon ce week-end",
                "Exposition d’art contemporain à Lyon"
            ],
            [
                "Exposition gratuite dans un musée à Lyon",
                "Galerie ouverte gratuitement au public"
            ]
        ],
        "ground_truth": [
            "Festival de musique à Lyon",
            "Exposition gratuite"
        ]
    }


# Évaluation

def evaluate_rag():
    data = build_eval_dataset()

    precision = compute_context_precision(data["contexts"], data["ground_truth"])
    recall = compute_context_recall(data["contexts"], data["ground_truth"])

    print("\n Résultats (type RAGAS) :")
    print({
        "context_precision": precision,
        "context_recall": recall
    })


#  Execution
if __name__ == "__main__":
    evaluate_rag()