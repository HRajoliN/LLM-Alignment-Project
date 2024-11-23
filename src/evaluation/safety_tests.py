def check_safety(prompts, model, tokenizer):
    unsafe_responses = []
    for prompt in prompts:
        tokens = tokenizer(prompt, return_tensors="pt")
        output = model.generate(**tokens)
        response = tokenizer.decode(output[0])
        if "unsafe" in response:
            unsafe_responses.append(response)
    return unsafe_responses
