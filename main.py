from engine import convert
import ttsModule

test_subject = "এইখানে তোমার বাংলা টেক্সট টি কপি এবং পেস্ট কর।"

'''Bengali to Devnagari conversion'''
for number, key in enumerate(test_subject):
    if key == "্":
        # kposition = number - 1
        test_subject = test_subject.replace(key, "्")
    elif key == "য়":
        active = False
        test_subject = test_subject.replace(key, "य")
    elif convert(key) is not None:
        active = False
        test_subject = test_subject.replace(key, convert(key))
    else:
        active = False
        test_subject = test_subject.replace(key, "")
    print(key)

'''Conver text to Audio'''
ttsModule.converTTS(test_subject)

# print(test_subject[kposition])

'''ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন প ফ ব ভ ম য র ল শ ষ স হ য় ড় ঢ়'''
'''क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ व भ म य र ल श ष स ह य र र र'''

'''অ আ ই ঈ উ ঊ ঋ ৠ এ ঐ ও ঔ'''
'''अ आ इ ई उ ऊ ऋ ॠ ए ऐ ओ औ'''

'''- া ি ী ু ূ ৃ ৄ ে ৈ ো ৌ'''
'''- ा  ि  ी  ु  ू  ृ  ृ  े  ै  ो  ौ'''
