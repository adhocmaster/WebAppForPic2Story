import gpt_2_simple as gpt2
from datetime import datetime

def RunGPT(_prompt, _run_name, _length, _temperature):
    all_text = 'GPT_alltext_fairytale'
    first_thirty = 'GPT_FirstThirtyLine'
    fairytale = 'fairytale'
    #f_target=open("out2.txt", "a+")
    r_name = _run_name
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name=r_name)
    temp = gpt2.generate(sess, run_name=r_name, return_as_list=True, length=_length, temperature=_temperature, prefix= _prompt, nsamples=1, batch_size=1 )
    return temp

 





