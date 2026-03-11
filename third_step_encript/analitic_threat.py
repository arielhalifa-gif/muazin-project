

how_many_threat_words = {}

def reset_dict(list_hige_threat_words, list_low_threat_words):
    for i in list_hige_threat_words:
        how_many_threat_words[i] = 0
    for i in list_low_threat_words:
        how_many_threat_words[i] = 0


def calculate_risk_level(total):
    #there are only 12 word of high risk and 8 of low risk
    percent_bds = (total/(12+8)) * 100
    return percent_bds


def calculate_threat_percentage(list_hige_threat_words, list_low_threat_words, stt_text):
    total_words = 0
    reset_dict(list_hige_threat_words, list_low_threat_words)
    for word in stt_text:
        if word in list_hige_threat_words:
            how_many_threat_words[word] += 2
            total_words += 2
        if word in list_low_threat_words:
            how_many_threat_words[word] += 1
            total_words += 1
    percent_bds = calculate_risk_level(total_words)
    return percent_bds