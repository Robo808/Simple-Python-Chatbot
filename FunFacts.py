#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import sys
import random

# Random facts taken from the https://bestlifeonline.com/random-obscure-facts/ website 


FunFacts = [
    'Competitive art used to be in the Olympics: Between 1912 and 1948, the Olympic Games awarded medals in sculpture, music, painting, and architecture, according to Smithsonian magazine. After a heated debate in the post-war years, the competitions were scrapped. John Copley of Britain won one of the final medals: At 73, he would be the oldest medalist in Olympic history if his silver, awarded for his 1948 engraving Polo Players, were still counted.' ,

    'A chef\'s hat has exactly 100 pleats: Bon Appétit magazine brings us this tasty tidbit. A chef\'s tall hat (officially known as a "toque") is traditionally made with 100 pleats, meant to represent the 100 ways to cook an egg.' ,

    "\"OMG\" usage can be traced back to 1917: One of the earliest uses?perhaps the earliest use?of \"OMG\" appeared in a letter to the then-member of Parliament, as The Atlantic reports. In 1917, British Navy Admiral John Arbuthnot Fisher wrote to Winston Churchill about rumors of new titles that would soon be bestowed. \"I hear that a new order of Knighthood is on the tapis,\" he wrote. \"O.M.G. (Oh! My God!)?Shower it on the Admiralty!\" OMG, indeed." ,

    "Some cats are actually allergic to humans: Though it's uncommon?since humans bathe more than your typical animal, and don't shed as much hair or skin?some animals can still be allergic to humans, according to Popular Science. (However, it's more often because of the perfume or cologne we wear, or the soap we use." , 

    "The majority of your brain is fat.: You can literally call someone a fathead, but it's still unkind: According to Psychology Today, 60 percent of human brain matter is made of fat." , 

    "Oranges aren't naturally occurring fruits: Oranges may be an iconic fruit, but they are not a naturally occurring one, as The Telegraph points out. In fact, oranges are a hybrid of tangerines and pomelos, also known as \"Chinese grapefruit,\" and they were originally green?not, well, orange. Oranges are a subtropical fruit, but now that they exist in more temperate climates, they lose their chlorophyll-induced green and become their more familiar color when the weather warms up." , 

    "High heels were originally worn by men.: In the 10th century, men in Europe adopted the now-gendered fashion choice of heels to make it easier to ride their horses: Adding heels to their boots made it easier to stay in their stirrups. As Slate explains, \"The Persian cavalry wore inch-high heels, and the trend spread to Europe. Since they showed that the wearer owned and maintained horses, high heels became associated with the upper class.\"" , 

    "Stop signs used to be yellow: In 1922, the American Association of State Highway Officials met to determine a standard design for stop signs, and that's where they decided on the color?yellow. Wait, what? Yes, according to Business Insider, stop signs were yellow because they thought that would grab drivers' attention. They'd also considered red, but there was no dye available at the time that wouldn't eventually fade. By 1954, however, sign makers had access to fade-resistant porcelain enamel, and could finally start making stop signs the red color we recognize today." , 
 
    "New York was briefly named \"New Orange.\": Yes, before it was the Big Apple, it was New Orange. As History reports, when the Dutch captured New York from the English in 1673, they renamed it New Orange in honor of William III of Orange. The following year, the English regained control and ditched the \"Orange.\"" , 

    "There was a successful Tinder match in Antarctica in 2014.: The dating app is popular across the globe, but it didn't have a connection on the least-inhabited continent until 2014, when a pair of research scientists?a man working at Antarctica's McMurdo Station and a woman camping a 45-minute helicopter ride away?found they had matched." , 

    "Most wasabi we eat in the U.S. isn't really wasabi: If you enjoy wasabi with your sushi, you'd probably be surprised to learn that most of the wasabi we consume in the U.S. isn't real wasabi made from the expensive wasabi root, according to the Chicago Tribune. The wasabi you're eating? That's white horseradish mixed with ground mustard seeds and green dye." , 

    "Green Eggs and Ham started as a bet: The Dr. Seuss classic grew out of a bet with his editor that he could not create a book using fewer than 50 different words. The editor, Random House founder Bennett Cerf, put?you guessed it?$50 on the line, and lost." ,

    "Andy Warhol inspired Louboutins' red soles: Louboutin shoes are known as much for their high price as for their red soles, but what many don't know is that the color was inspired by Andy Warhol. According to The New Yorker, Warhol's drawing Flowers caught Christian Louboutin's eye and gave him the idea?with the aid of an assistant's red nail polish?to add the color to the bottom of the kicks." ,

    "There is a fruit that tastes like chocolate pudding: Black sapote has another irresistible name: the chocolate pudding fruit. According to Good Morning America, the fruit?native to Central and South America?tastes like sweet custard with a hint of chocolate. When it's fully ripe, the flavor (and consistency) has been described as a dead ringer for chocolate pudding." ,

    "Too much water can kill you: Drinking too much water can be deadly. When guzzling a lot of liquid, you can suffer from water intoxication or hyponatremia, which occurs after an obscene amount of water is consumed, often during endurance events when participants are also losing sodium through their sweat. There have been many notable cases, including the 2002 Boston Marathon competitor Cynthia Lucero, who died from overhydration." ,

    "The hottest temperature ever recorded on Earth was 2 billion degrees kelvin: To give you a sense of how hot that is: The interior of our sun is only about 15 million degrees kelvin. Researchers at Sandia National Laboratories produced the record-breaking temperature in their lab using a superheated gas, equal to about 3.6 billion degrees Fahrenheit, which is? significantly warmer than any temperature your oven could reach." ,

    "The moon is (slowly) slowing the Earth's rotation: Every one hundred years, the moon adds approximately 1.4 milliseconds to a day. While this may be minuscule, it does add up: When dinosaurs roamed the planet, days were 23 hours long, according to NASA." , 

    "You might be drinking water that is older than the solar system: As the The New York Times reports, water on our planet may have originated from ice specks floating in a cosmic cloud 4.6 billion years ago. Not impressed? It follows that \"the same liquid we drink and that fills the oceans may be millions of years older than the solar system itself.\" Something to keep in mind while you're staying hydrated!", 

    "Queen Elizabeth II is a trained mechanic: Yes, the queen is actually quite handy. When she was 16, she joined the British employment agency the Labour Exchange, where she learned the basics of truck repair, including how to change a tire and repair engines. Nowadays, she has others who can do such things for her, but isn't it nice to know that if one of her cars broke down, she might be able to get it up and running? Perhaps that early understanding of automobiles inspired Queen Elizabeth II's lifelong love of cars. Her collection of vintage Rolls-Royces, Daimlers, Bentleys, and other brands is estimated to be worth £10 million, according to Business Insider."

    "Moonshiners used \"cow shoes\" to disguise their footprints during Prohibition: To keep their whiskey stills from being spotted, moonshiners during prohibition would often wear \"cow shoes,\" with wooden blocks attached to the bottoms to make their footprints resemble a cow's." ,

    "It takes 364 licks to get to the center of a Tootsie Pop: At least, according to some studies. Engineering students from Purdue University designed a licking machine?built to function like a real human tongue?and found that it took an average of 364 licks to get to the center of a Tootsie Pop. For what it's worth, 20 volunteers tried the experiment using their actual tongues and averaged 252 licks. And other studies averaged out to 144 (Swarthmore Junior High School) and 411 (University of Michigan) licks. Honestly, just bite it." ,

    "Tree rings get wider during wet years: You probably already know that tree rings can tell you how old a tree is. But they can also show you the conditions of a given year, according to NASA: Thinner rings appear during drought years, and thick ones mean there was significant rainfall." ,

    "The hottest inhabited place in the world is in Ethiopia: Dallol, Ethiopia, has the highest average temperature of any inhabited place on Earth. Climate data recorded between 1960 and 1966 had the average high at 106 degrees Fahrenheit. (Even in the winter, the average highs were between 97 and 98 degrees.)" ,

    "Hot water freezes faster than cold water: Crazy, right? A number of explanations have been suggested for \"the Mpemba effect,\" including one that posits warm containers conduct heat more efficiently, and another that suggests warm water evaporates faster." ,

    "Dolphins have names for one another: You've probably heard that dolphins are pretty clever, but this is especially impressive: According to National Geographic, dolphins actually have names for one another, using a unique whistle to distinguish between different members within their pod." ,

    "Shel Silverstein wrote the song \"A Boy Named Sue\": The well known Johnny Cash song was actually penned by the famous children's book author and poet behind works such as Where the Sidewalk Ends, The Giving Tree, and A Light in the Attic. He also wrote songs performed by Emmylou Harris, Waylon Jennings, Loretta Lynn, and more." ,

    "The bowler hat was invented as safety measure: The familiar bowler hat may look fashionable, but it began as a purely practical item?a riding helmet meant to protect riders from branches and other obstacles, according to The Telegraph. It was designed by London hatmakers Thomas and William Bowler, hence the name." ,

    "Sea otters hold hands while they sleep: This ridiculously cute behavior is an effort to avoid floating away from their partner during sleep. Sometimes they hold hands in groups, producing a \"raft.\"" ,

    "Platform shoes once symbolized status: Raised platform shoes (known as \"buskins\") were worn by tragic actors in Ancient Greece to symbolize their superiority over comic actors, who wore plain socks." ,

    "Weeds can be healthy: Though we usually just pull them up and toss them into the trash, some weeds have nutritious properties. For example, dandelions are loaded with vitamins A, C, and K?not to mention calcium, iron, and potassium. So consider repurposing those weeds and making them into a salad."

    "The French word for dandelion refers to a bodily function: Be careful about drinking any dandelion wine?the French word for dandelion, pissenlit, means \"wet the bed.\" The name comes from the fact that dandelion leaves have diuretic properties." ,

    "Winston Churchill's mother was from Brooklyn: Though he is one of the UK's most famous leaders, wartime prime minister and career politician Churchill had U.S. roots. His mother, Lady Randolph Churchill, was born in Cobble Hill, Brooklyn." ,

    "Toto the dog was once a cow: In the original 1902 stage version of The Wonderful Wizard of Oz, Dorothy did not have a dog but a faithful cow named Imogene. While L. Frank Baum's book features the Toto we know and love, his adaptation opted for the larger animal. \"It may seem a long jump from a dog to a cow, but in the latter animal we have a character that really ought to amuse the youngsters,\" he said in 1904." ,

    "Reno is farther west than Los Angeles: Don't believe us? Look at a map!" ,

    "Giant squids have the largest eyes of any animal on Earth: If you're not sufficiently scared of giant squids, consider that their eyes are 11 inches across. That makes them the largest known eyes in the animal kingdom." ,

    "Speed dating was invented by a rabbi: Rabbi Yaacov Deyo, based in Beverly Hills, California, created the concept of speed dating in 1998, according to The New York Times. He brought together a handful of single men and women for some matchmaking at a Peet's Coffee, and romance and efficiency proved to be a perfect match.", 

    "The blob of toothpaste that sits on your toothbrush has a name: It's called a \"nurdle,\" and there was a lawsuit over which toothpaste company had the right to depict it." ,

    "Parrots have the power of reason: In addition to humans and chimps, the African grey parrot has been found to be able to reason?approximately at the level of a three-year-old kid, according to Smithsonian magazine. In an experiment, the parrots were presented with a pair of closed canisters, and shown that there was food inside one of them. When the parrots were given the chance to choose between canisters, they consistently selected the one with food."
]