MODEL = "v4_hellaswag"

paths = {   'algebraic_stack': f's3://ai2-benb/corpus_scores/{MODEL}/proof-pile-2/v0_decontaminated/documents/algebraic-stack/train',
    'all_red_pajama': f's3://ai2-benb/corpus_scores/{MODEL}/redpajama/v1',
    'arxiv': f's3://ai2-benb/corpus_scores/{MODEL}/redpajama/v1_decon_fix/documents/train/arxiv',
    'c4': f's3://ai2-benb/corpus_scores/{MODEL}/c4/v1_7-dd_ngram_dp_030-qc_cc_en_bin_001-fix',
    'cc_eli5_oh_top10p': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/eli5_oh_top10p',
    'cc_eli5_oh_top20p': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/eli5_oh_oh_top20p',
    'cc_news': f's3://ai2-benb/corpus_scores/{MODEL}/cc-news/v3',
    'cc_og_eli5_oh_top10p': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/og_eli5_oh_top10p',
    'cc_tulu_qc_top10': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/tulu_qc_top10',
    'dclm_fw_top10': f's3://ai2-benb/corpus_scores/{MODEL}/dclm/v0_fw_top10p',
    # 'dclm_mmlu_top10': f's3://ai2-benb/corpus_scores/{MODEL}/dclm/regression_synthetic_mmlu_10p/documents/1t',
    'falcon': f's3://ai2-benb/corpus_scores/{MODEL}/falcon-refinedweb/v2-frac_005_100-qc_cc_multi_bin-paloma-rep-pii',
    'falcon_eli5_oh_top10p': f's3://ai2-benb/corpus_scores/{MODEL}/falcon-refinedweb/eli5_oh_top10p',
    'falcon_eli5_oh_top20p': f's3://ai2-benb/corpus_scores/{MODEL}/falcon-refinedweb/eli5_oh_oh_top20p/documents/',
    'falcon_og_eli5_oh_top10p': f's3://ai2-benb/corpus_scores/{MODEL}/falcon-refinedweb/og_eli5_oh_top10p',
    'falcon_tulu_qc_top10': f's3://ai2-benb/corpus_scores/{MODEL}/falcon-refinedweb/tulu_qc_top10',
    'fineweb_edu_dedup': f's3://ai2-benb/corpus_scores/{MODEL}/fineweb-edu-dedup/v0',
    'gutenberg_books': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/v1_6-decontaminated/documents/books',
    'megawika': f's3://ai2-benb/corpus_scores/{MODEL}/megawika/v1',
    'pes20_stem_papers': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/v1_6-decontaminated/documents/pes2o',
    'pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top10p': f's3://ai2-benb/corpus_scores/{MODEL}/dclm/pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top10p/documents/1t',
    'pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top20p': f's3://ai2-benb/corpus_scores/{MODEL}/dclm/v1_pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top20p/documents/1t/',
    'prox_fineweb_pro': f's3://ai2-benb/corpus_scores/{MODEL}/prox_fineweb_pro/v0',
    'reddit': f's3://ai2-benb/corpus_scores/{MODEL}/reddit/v5-dedupe-pii-nsfw-toxic-fuzzydd-length',
    'regression_synthetic_20epochs_bs640_lf1_lre35_top10p': f's3://ai2-benb/corpus_scores/{MODEL}/dclm/regression_synthetic_20epochs_bs640_lf1_lre35_top10p/documents/1t',
    'regression_synthetic_20epochs_bs640_lf1_lre35_top20p': f's3://ai2-benb/corpus_scores/{MODEL}/dclm/regression_synthetic_20epochs_bs640_lf1_lre35_top20p/documents/1t',
    'stackexchange': f's3://ai2-benb/corpus_scores/{MODEL}/redpajama/v1_decon_fix/documents/train/stackexchange',
    'starcoder': f's3://ai2-benb/corpus_scores/{MODEL}/starcoder/v0_decontaminated_doc_only',
    'tulu': f's3://ai2-benb/corpus_scores/{MODEL}/tulu_flan/v2-decontaminated-60M-shots_all-upweight_1-dialog_false-sep_newline/documents/train',
    'web_rest': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/v1_7-dd_ngram_dp_030-qc_cc_en_bin_001/documents/cc_en_tail',
    'wikipedia_wikibooks': f's3://ai2-benb/corpus_scores/{MODEL}/olmo-mix/v1_6-decontaminated/documents/wiki',
    'DCLM-baseline': f's3://ai2-benb/corpus_scores/{MODEL}/dclm/raw/hero-run-fasttext_for_HF/filtered/OH_eli5_vs_rw_v2_bigram_200k_train/fasttext_openhermes_reddit_eli5_vs_rw_v2_bigram_200k_train/processed_data'
}

sources_sizes = {
    "gutenberg_books": 2_627_896_053,
    "pes20_stem_papers": 28_604_876_365,
    "wikipedia_wikibooks": 3_689_204_524,
    "megawika": 2_281_051_092,
    "stackexchange": 9_814_791_671,
    "arxiv": 13_986_831_288,
    "algebraic_stack": 6_311_288_265,
    "openwebmath": 6_367_150_300,
    "tulu": 8_268_453_782,
    "cc_news": 7_130_708_273,
    "starcoder": 131_887_652_399,
    "c4_debug": 827_856_324,
    "c4": 69_220_588_954,
    "reddit": 39_972_006_511,
    "falcon": 228_202_479_465,
    "web_rest": 299_211_329_457,
    "all_red_pajama": 625_652_417_451,
    "cc_eli5_oh_top10p": 51_306_739_746,
    "falcon_eli5_oh_top10p": 21_730_127_205,
    "cc_eli5_oh_top20p": 83_234_747_123,
    "falcon_eli5_oh_top20p": 59_690_132_487,
    "cc_og_eli5_oh_top10p": 49_047_630_489,
    "falcon_og_eli5_oh_top10p": 24_874_205_085,
    "prox_fineweb_pro": 41_361_594_483,
    "fineweb_edu_dedup": 96_100_913_800,
    "cc_tulu_qc_top10": 41_843_452_876,
    "falcon_tulu_qc_top10": 22_614_162_276,
    "pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top10p": 41_037_912_102,
    "pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top20p": 85_531_708_515,
    "regression_synthetic_20epochs_bs640_lf1_lre35_top10p": 53_320_429_656,
    "regression_synthetic_20epochs_bs640_lf1_lre35_top20p": 124_365_177_166,
    "dclm_fw_top10": 49_232_730_070,
    "dclm_ft7percentile_fw3": 108_986_400_784,
    "dclm_mmlu_top10": 49_939_303_843,
    "dclm_mmlu_top3": 63_465_963_452,
    "dclm_fw_top3": 59_044_721_273,
    "DCLM-baseline": 3857122337647
}


mixtures = {
    "no_math": ['gutenberg_books', 'wikipedia_wikibooks', 'megawika', 'stackexchange', 'arxiv', 'tulu', 'cc_news', 'starcoder', 'c4', 'reddit', 'falcon', 'web_rest'],
    "no_code": ['gutenberg_books', 'pes20_stem_papers', 'wikipedia_wikibooks', 'megawika', 'arxiv', 'algebraic_stack', 'openwebmath', 'tulu', 'cc_news', 'c4', 'reddit', 'falcon', 'web_rest'],
    "no_math_no_code": ['gutenberg_books', 'wikipedia_wikibooks', 'megawika', 'arxiv', 'tulu', 'cc_news', 'c4', 'reddit', 'falcon', 'web_rest'],
    "no_reddit": ['gutenberg_books', 'pes20_stem_papers', 'wikipedia_wikibooks', 'megawika', 'stackexchange', 'arxiv', 'algebraic_stack', 'openwebmath', 'tulu', 'cc_news', 'starcoder', 'c4', 'falcon', 'web_rest'],
    "no_flan": ['gutenberg_books', 'pes20_stem_papers', 'wikipedia_wikibooks', 'megawika', 'stackexchange', 'arxiv', 'algebraic_stack', 'openwebmath', 'cc_news', 'starcoder', 'c4', 'reddit', 'falcon', 'web_rest'],
    "baseline": ['gutenberg_books', 'pes20_stem_papers', 'wikipedia_wikibooks', 'megawika', 'stackexchange', 'arxiv', 'algebraic_stack', 'openwebmath', 'tulu', 'cc_news', 'starcoder', 'c4', 'reddit', 'falcon', 'web_rest'],
    "redpajama": ["all_red_pajama"],
    "falcon": ["falcon"],
    "falcon_and_cc": ["falcon", "web_rest"],
    "c4": ["c4"],
    "prox_fineweb_pro": ["prox_fineweb_pro"],
    "fineweb_edu_dedup": ["fineweb_edu_dedup"],
    "falcon_and_cc_eli5_oh_top10p": ["cc_eli5_oh_top10p", "falcon_eli5_oh_top10p"],
    "falcon_and_cc_eli5_oh_top20p": ["cc_eli5_oh_top20p", "falcon_eli5_oh_top20p"],
    "falcon_and_cc_og_eli5_oh_top10p": ["cc_og_eli5_oh_top10p", "falcon_og_eli5_oh_top10p"],
    "falcon_and_cc_tulu_qc_top10": ["cc_tulu_qc_top10", "falcon_tulu_qc_top10"],
    "pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top10p": ["pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top10p"],
    "pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top20p": ["pos_eli5_oh_neg_dclm_refinedweb_steps_2000_lr3e4_top20p"],
    "regression_synthetic_20epochs_bs640_lf1_lre35_top10p": ["regression_synthetic_20epochs_bs640_lf1_lre35_top10p"],
    "regression_synthetic_20epochs_bs640_lf1_lre35_top20p": ["regression_synthetic_20epochs_bs640_lf1_lre35_top20p"],
    "dclm_mmlu_top10": ["dclm_mmlu_top10"],
    "dclm_fw_top10": ["dclm_fw_top10"],
    # "dclm_ft7percentile_fw2": ["dclm_ft7percentile_fw2"],
    # "dclm_ft7percentile_fw3": ["dclm_ft7percentile_fw3"],
    "DCLM-baseline": ["DCLM-baseline"],
}