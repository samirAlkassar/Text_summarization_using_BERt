from transformers import pipeline, BartTokenizer, BartForConditionalGeneration

# Load BART tokenizer and model
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Define input text
# text = """
#       Cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body.[2][7] These contrast with benign tumors, which do not spread.[7] Possible signs and symptoms include a lump, abnormal bleeding, prolonged cough, unexplained weight loss, and a change in bowel movements.[1] While these symptoms may indicate cancer, they can also have other causes.[1] Over 100 types of cancers affect humans.[7]

# Tobacco use is the cause of about 22% of cancer deaths.[2] Another 10% are due to obesity, poor diet, lack of physical activity or excessive drinking of alcohol.[2][8][9] Other factors include certain infections, exposure to ionizing radiation, and environmental pollutants.[3] In the developing world, 15% of cancers are due to infections such as Helicobacter pylori, hepatitis B, hepatitis C, human papillomavirus infection, Epstein–Barr virus and human immunodeficiency virus (HIV).[2] These factors act, at least partly, by changing the genes of a cell.[10] Typically, many genetic changes are required before cancer develops.[10] Approximately 5–10% of cancers are due to inherited genetic defects.[11] Cancer can be detected by certain signs and symptoms or screening tests.[2] It is then typically further investigated by medical imaging and confirmed by biopsy.[12]
# """


def summarize(text):
    # Split input text into smaller chunks
    max_chunk_size = 1024
    chunks = [text[i:i+max_chunk_size]
              for i in range(0, len(text), max_chunk_size)]

    # Generate summaries for each chunk
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=60, min_length=30)
        summaries.append(summary[0]['summary_text'])

    # Combine individual summaries into a single summary
    final_summary = ' '.join(summaries)
    return final_summary


# Print the final summary
# summary = summarize(text)
# print(summary)
