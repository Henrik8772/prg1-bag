Jag har gjort ett "Inventory" / påse.

Du kan i påsen savea items antingen en efter en eller skriva flera olika items genom att skilja på dem med ett komma tecken. samt så kan man nu skriva in exempelvis 6 stone och då displayar den 6x stone i ditt inventory.

Den där delen av programmet använder sig av import re vilket är RegEx eller om man ska säga hela namnet Regular Expression, det är den som fixar att man kan skriva 6 stone och den stoppar in 6x stone i inventory. 

samt kan man också i inventoryt hitta saker i inventoryt där den visar hur många av det du söker du har samt om du har det eller inte. 

jag har gjort  så du kan remova saker från inventoryt samt också gjort så att du kan exita inventoryt vilket avslutar programmet. 

jag använder en while loop för påsens kommandon och de grejerna samt så använder jag en def innan while loopen för systemet med att kunna skriva 6 stone och få 6x stone i inventoryt. 

det finns några veriablar utanför loopen också.

inventroyt sorteras varje gång du sparar ny items samt när du tarbort items.

**OBS! gjorde ingen max items eller max weight eftersom det är legit ganska jobbigt eftersom max items då måste jag antingen göra alla items samma globala max eller att du kan max ha typ 10 items totalt eller göra det mer complext med att göra så att varje item har en max limit vilket betyder mer listor, och den andra med max weight kräver också en lista med specifika item weight values vliket betyder varje gång man lägger till ett item måste man lägga till en vikt för den också. kunde definitivt gjort en max items och sedan en för resurser som wood, stone, fiber, metal och sådant skit, kan fortfarande göra det om du vill för jag kan gärna göra det men då kan du skriva det i privat kommentar.** 

detta är länken till regex guide på vad den gör och hur man använder den ungefär, jag sökte up på google om sätt att gör det där med att kunna savea mer av en sak samtidigt utan att skriva namnet om och om igen då var detta den mest använda import och kommandona jag hittade.

https://www.w3schools.com/python/python_regex.asp
