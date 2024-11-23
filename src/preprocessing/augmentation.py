from nlpaug.augmenter.word import SynonymAug

def augment_text(text, n=3):
    """
    Perform text augmentation using synonyms.
    """
    aug = SynonymAug(aug_src="wordnet")
    return [aug.augment(text) for _ in range(n)]
