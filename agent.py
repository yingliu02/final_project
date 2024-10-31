import logging


def load_model(model_name: str):
    # TODO: actually load the model using transformers
    # model = transformers.AutoModelForCausalLM.from_pretrained(model_name)
    # return model.generate
    return generate_response


def generate_response(prompt):
    # TODO: actually generate a response using the model
    return "I'm sorry, I cannot do that."
