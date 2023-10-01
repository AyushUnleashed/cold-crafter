GPT_3_INPUT_COST = 0.0015  # Cost per 1000 input tokens for GPT-3
GPT_3_OUTPUT_COST = 0.0020  # Cost per 1000 output tokens for GPT-3
GPT_4_INPUT_COST = 0.03  # Cost per 1000 input tokens for GPT-4
GPT_4_OUTPUT_COST = 0.06  # Cost per 1000 output tokens for GPT-4
MODEL_GPT_35_TURBO = "gpt-3.5-turbo"
MODEL_GPT_4 = "gpt-4"


def cost_calculator(MODEL_NAME, prompt_tokens, completion_tokens):
    if MODEL_NAME == MODEL_GPT_35_TURBO:
        input_cost = (prompt_tokens / 1000) * GPT_3_INPUT_COST
        output_cost = (completion_tokens / 1000) * GPT_3_OUTPUT_COST
    elif MODEL_NAME == MODEL_GPT_4:
        input_cost = (prompt_tokens / 1000) * GPT_4_INPUT_COST
        output_cost = (completion_tokens / 1000) * GPT_4_OUTPUT_COST
    else:
        raise ValueError("Unsupported model name")

    total_cost = input_cost + output_cost
    return total_cost
