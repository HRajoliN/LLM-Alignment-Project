def run_safety_tests(model, tokenizer, test_prompts):
    """
    Check model responses for safety.
    """
    unsafe_responses = []
    for prompt in test_prompts:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs)
        response = tokenizer.decode(outputs[0])
        if "unsafe_keyword" in response:
            unsafe_responses.append(response)
    return unsafe_responses
