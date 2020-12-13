from django.shortcuts import render
from PyDictionary import PyDictionary

def index(request):

   word = request.GET.get("word","")
   htmlbody = ""

   if word != "":
      dictionary = PyDictionary()
      htmlbody = "<h1 style='color:blue'>" + word + ":</h1><br>"
      try:
         meaning = dictionary.meaning(word)

         for key in meaning:
            htmlbody = htmlbody + "<h3 style='color:red'>" + str(key) + "</h3>"

            for items in meaning[key]:
               htmlbody = htmlbody + "<h4>" + str(items) + '</h4>'

            htmlbody += "<br>"

         synonyms = dictionary.synonym(word)
         htmlbody += "<b style ='text-size:large; color:red'> Synonyms: </b>"

         for items in synonyms:
            htmlbody += "<b>" + items + "," + "</b>"

         htmlbody += "<br>"

         antonym = dictionary.antonym(word)
         htmlbody += "<b style ='text-size:large; color:red'> Antonyms: </b>"

         for items in antonym:
            htmlbody += "<b>" + items + "," + "</b>"

         htmlbody += "<br><br>" + "<b style ='text-size:large; color:red'> Hindi: </b>"
         try:
            htmlbody += "<b>" + str(dictionary.translate(word,'hi')) +" </b>"
         except:
            htmlbody += "<b>No Hindi translations</b>"


      except:
         htmlbody = htmlbody + "<h3 style='color:red'>" + "Sorry, We were unable to find any meaning for this word" + "</h3>"

   params = {'body':htmlbody}
   return render(request,"index.html", params)


