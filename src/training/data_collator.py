from transformers import DataCollatorForSeq2Seq

def create_data_collator(tokenizer):
    """
    Create a data collator for sequence-to-sequence tasks.
    """
    return DataCollatorForSeq2Seq(tokenizer)
