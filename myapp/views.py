from django.shortcuts import render

def main(request):
    return render(request,'main.html')

def result(request):
    text = request.GET['totaltext']
    split_text = text.split()

    word_dict={}
    for word in split_text:
        if word in word_dict:
            word_dict[word]+=1    #{'안녕': 1+1} -->2번
        else:
            word_dict[word] = 1     #{'안녕':1} -->1번
    return render(request,'result.html', {'written_text': text, 'word_list':len(split_text), 'word_count':word_dict.items()})
