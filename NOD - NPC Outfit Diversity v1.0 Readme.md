NOD - NPC Outfit Diversity
v1.0
by Lucevar & the Morrowind Community

## Introduction 
With NPC Outfit Diversity, you can enjoy a more colorful and varied fashion scene in Vvardenfell (and Solstheim and Mournhold). NOD uses equipment created by modders to add new and unique outfits for NPCs, making them more unique and visually appealing. The overall aesthetic was inspired by mods like Dunmer Nobles Overhaul, Buoyant Armigers Armor, Investigations at Tel Eurus, and Yul Marshee and the Visage of Mzund - colourful, fun, and lore-extending, but still respectful of the original themes. 

It covers both equipment (armor, clothing, and weapons) as well as general appearance (heads and hairs). Which means it should probably be called "NPC Appearance Diversity", buuuut I like NOD better as an acronym.

## Philosophy
I had several goals in mind while making this mod:

* Add more colour and variety to Vvardenfell's fashion scene. I've been playing this game for 20 years, it was time to freshen it up.
* Add colour and pizzazz without breaking the lore. We've all had a rough few years, and I've come out of that wanting more colour and fun rather than grim-dark gritty realism, which I tended to prefer in the past. And, look. I really like waistcoats. What can I say?
* Make use of the wonderful clothes, armors, weapons, heads, and hairs that the community has created over the past two decades, and really show them off in a way that does them justice. Instead of being shoved into leveled lists or into the inventory of a lonely shopkeeper in the middle of nowhere, NOD puts them on display. 
* NOD also puts them into leveled lists and the worldspace, of course, so that you can have as much drip as the NPCs. 
* Smooth out conflicts between some existing NPC enhancement mods, remove any lore-breaking items, and rebalance stats so they fit in well with each other and with the vanilla equipment progression curve.
* Maintain balance. Many NPCs now have better equipment, meaning that you'll have a tougher fight if you want to get your hands on it. The strongest sets of equipment are rare. 
* Where possible, maintain compatibility with the original mods. 
* Exhaustively document changes so that it's easy to check compatibility. 
* Make faction, class, and cultural affiliations more obvious and distinct.
* Make every NPC unique, in a way that respects their personality and position in life. 
* Iconic NPCs are less likely to be changed. Caius, Jiub, M'Aiq, and Divayth aren't changed, for example. 
* Make sure the vanilla items still get used regularly. I don't want to get rid of them, just add more variety. 



## Features - Core
This is just a broad overview of NOD's features, and doesn't list every chage. For a detailed changelist per-NPC, please see the changelist in 00 Core/docs/npcs.md

### Heads and Hair
### Cultural Affiliation
### Class-Based Changes
### Equipment Variants
### New NPCs

## Features - Addons
### MWSE - Fashionwind Addon
* Requires Onion - Layered Accessories. Gives NPCs a variety of items of headgear, including masks, glasses, monocles, and goggles. Many NPCs already get facemasks in the Core esm - the masks in the addon are for NPCs who are already wearing a hood or helmet. 
### MWSE - Fashionwind Bosmer Horns & Antlers Addon
* Requires Onion - Layered Accessories. Makes Bosmer a little closer to their concept art by adding horns and antlers to a number of them. One of the biggest departures from the vanilla aesthetic this mod makes, but I'm enjoying the look. 
### MWSE - Fashionwind Ra'Gruzgob Addon
* Requires Onion - Layered Accesories. Makes Ra'Gruzgob the pretty kitty he was always meant to be. Are they real? Are they an illusion? Who knows.
### Cinia Urtius Addon
* The vanilla game left the master trainer for Medium Armor out entirely. This adds her back. That's all it does (she gets a new appearance in the core esm).
### Streamer Safety Addon
* The terms of service of sites like Twitch forbid streamers from showing nudity, which makes our favourite naked nords and dancing ladies a trifle problematic. This addon, which is compatible with either engine, gives the Nords a loincloth and the dancers a skimpy outfit to cover up with.

## Features - Patches
### MacKom heads patch
* The core folder uses vanilla/Westly compatible meshes for the Dunmer nobles hairs. This patch restores the original, MacKom-compatible meshes.



# Requirements
* Assets: [**Tamriel Data**](https://www.nexusmods.com/morrowind/mods/44537) and [**OAAB Data**](https://www.nexusmods.com/morrowind/mods/49042). The rest are bundled here.
* Engine: The core mod should work in either OpenMW or MCP-MWSE-Morrowind. There are some reflection-mapped items that may not work well in vanilla without MCP, but the mod should still work.
* Body Replacer: Requires Better Bodies. Which version of Better Bodies you use shouldn't matter - I use [**Better Bodies 3.1 (Better Beasts)**](https://www.nexusmods.com/morrowind/mods/48387) by OverCellus. It MIGHT work with other bodies, mostly, but it will probably require you to make an addon to remove some outfits. I haven't tested it with anything except Better Bodies. 
* Addons: Most, but not all, of the addons require the core esm. Anything in a folder marked 'MWSE' will require MWSE, likewise anything marked 'OpenMW' requires that engine. 
* Fashionwind addons: Require both an up-to-date MWSE and [**Onion - Layered Accessories**](https://www.nexusmods.com/morrowind/mods/50352) by Safebox.



# Installation
1. Install [**Tamriel Data**](https://www.nexusmods.com/morrowind/mods/44537) and register the three bsas.
2. Install [**OAAB Data**](https://www.nexusmods.com/morrowind/mods/49042).
3. Install [**Better Bodies 3.1 (Better Beasts)**](https://www.nexusmods.com/morrowind/mods/48387), or your preferred version of Better Bodies.
4. If you're using the vanilla engine, install [**Morrowind Code Patch**](https://www.nexusmods.com/morrowind/mods/19510).
5. If you're using the vanilla engine, install [**MGE XE**](https://www.nexusmods.com/morrowind/mods/41102). 
6. Use MO2 to install NOD, or if doing it manually, copy the contents of the 00 Core folder into Morrowind/Data Files
7. If you're using the MWSE Fashionwind addons, install [**Onion - Layered Accessories**](https://www.nexusmods.com/morrowind/mods/50352)
8. Copy any addons you wish to use into Morrowind/Data Files.
9. Enable NOD - Core.esm and any addons with esps in the launcher or Wrye Mash.
10. If you're on the vanilla engine, use [**tes3merge**](https://www.nexusmods.com/morrowind/mods/46870) to generated a merged objects file. This will reduce incompatibilities with other mods by merging object records and leveled lists. I believe OpenMW has an equivalent called delta plugin.
10. Start a new game. Due to the way Morrowind stores NPC data in save games, any NPCs you've already met before installing NOD won't have their new appearance until you start a new game.



# Compatibility
In general, because NOD is an esm, it will load very early in your load order and therefore be compatible with most mods. Other mods that require NPC changes will either be patched by creating a merged objects file with tes3merge, or simply load later than NOD and 'win' the load order battle. In that case, you might miss out on some of the new outfits, but it's more important that eg quest mods are able to make their changes, since NOD is only cosmetic.

## Included or partially included, but compatible
I did my best to maintain compatibility with the original mods. That wasn't always possible, but the following are safe to run alongside NOD, although there might be some oddities eg the same item of clothing with a different name or stats. A huge thanks to all the modders who've allowed me to include their work. More detailed credits available in the credits section, or in the original readmes which are bundled. Please do download the originals and endorse them.

* [**Concept Art Dunmer Helmets**](https://www.nexusmods.com/morrowind/mods/52043) by RuffinVangarr  
In NOD, the helmets are distributed to netchimen and various House enforcers, as well as added to leveled lists. Compatible with the original but redundant.
* [**Daedric Telvanni Robe**](https://www.nexusmods.com/morrowind/mods/49652) by RuffinVangarr  
Included in NOD, but you may wish to use the original as well. NOD gives the robe to Gothren, so it isn't available until late game; the original places it somewhere more accessible.  
* [**The Ebony Warrior**](https://www.nexusmods.com/morrowind/mods/48564) by RuffinVangarr  
The armor is included in NOD, but not the encounter with the warrior. You can run them alongside each other to test your mettle against the warrior.
* [**Dreamers Expansion**](https://www.nexusmods.com/morrowind/mods/42990) by Aoimevelho  
A small number of torn/dirty clothes from Dreamers Expansion are renamed and used in NOD. None of Dreamer Expansion's NPC or leveled list changes are used - you should download the original for a proper dreamers overhaul.  
* [**Hilgya the Seamstress**](https://www.nexusmods.com/morrowind/mods/49766) by Plangkye  
Original downloads on MMH [**here**](https://mw.modhistory.com/download-21-13102) and [**here**](https://mw.modhistory.com/download-21-12474). Compatible with the original but redundant; run alongside if you want the shop in Dagon Fel, but there will be some duplicate items of clothing.
* [**Dim's Khajiit Head and Hair Pack**](https://www.nexusmods.com/morrowind/mods/51977) by DimNussens  
Original is a modders resource; running them together is redundant but no harm done.  
* [**FCOT**](http://download.fliggerty.com/download-55-751) by Westly
A small number of clothes from FCOT are renamed and included in NOD, but the merchant and the majority of clothes are not. Compatible to run together - you need to use both if you want to get the full set of FCOT clothes. The only potential issue is there may be some duplicates with different/names stats. 
* [**Danke's Armors**](https://www.nexusmods.com/morrowind/mods/45114) by Danke  
About 60% of the armors are used, distributed either to their intended owners or to other NPCs. Compatible but redudant with the original; you may still wish to use it if you want a non-violent way to gain the armors, or if you want the armors I haven't included. 
* [**Netch adamantium armour integrated**](https://www.nexusmods.com/morrowind/mods/49641) by RandomPal and Cythus  
Included in NOD and distributed to NPCs. Safe but redundant to run together.
* [**Many Cloth Helms**](https://www.nexusmods.com/morrowind/mods/49282) by Markond  
NOD distributes the scarfs to NPCs. Running them together is redundant and you'll get item duplicates, but that's harmless. 
* [**Redvayn's Humble Headgear**](https://www.nexusmods.com/morrowind/mods/48647) by Shehriazad  
Most of the hats are included in NOD. For the unique hats and the quest, run the original alongside NOD. 
* [**Complete and Revised Nordic Iron Armor**](https://www.nexusmods.com/morrowind/mods/50166) by RuffinVangarr  
* [**Complete Duke's Guard Silver**](https://www.nexusmods.com/morrowind/mods/50481) by RuffinVangarr  
* [**Fashionwind - MWSE Glasses and Goggles V2**](https://www.nexusmods.com/morrowind/mods/50448) by RuffinVangarr  
* [**Fashionwind - MWSE Masks and Facewraps**](https://www.nexusmods.com/morrowind/mods/51610) by RuffinVangarr  
* [**Concept Art Daedric Helmets**](https://www.nexusmods.com/morrowind/mods/49534) by RuffinVangarr  
* [**Dwemer Scrap Armor**](https://www.nexusmods.com/morrowind/mods/47665) by RuffinVangarr 
* [**Heavy Chitin Armor**](https://www.nexusmods.com/morrowind/mods/47684) by RuffinVangarr 
* [**Complete and Revised Dreugh Armor**](https://www.nexusmods.com/morrowind/mods/49092) by RuffinVangarr 
* [**Complete and Revised Imperial Studded Leather Armor**](https://www.nexusmods.com/morrowind/mods/49301) by RuffinVangarr
RuffinVangarr has very generously allowed me to include all the above mods. NOD is compatible with the originals, but redundant.
* [**Fashionwind - MWSE Horns and Antlers**](https://www.nexusmods.com/morrowind/mods/51209) by RuffinVangarr  
The horns and anglers are included in NOD, but you may wish to run the original alongside for the merchant with her unique dialogue.

## Included or partially included
Do not run together with NOD (but please do download and endorse the originals). Again, a huge thanks to all the modders who've allowed me to include their work. More detailed credits available in the credits section, or in the original readmes which are bundled.

* [**Properly Clothed NPCs**](https://www.nexusmods.com/morrowind/mods/48870) by RandomPal
Alternative outfit replacer (and 80% included in NOD). Use one or the other. Properly Clothed NPCs is also included in VFWE. 
* [**Sacred Necromancer Armor**](https://www.nexusmods.com/morrowind/mods/51651) by RuffinVangarr
Included and slightly extended in NOD (dialogue tweaks, sacred necromancers added to Ghostgate).
* [**Necromancer Robes**](https://www.nexusmods.com/morrowind/mods/51775) by RuffinVangarr
Included and slightly extended in NOD (all the equipment alternatives are available now).
* [**Ceremonial Adamantium Armor**](https://www.nexusmods.com/morrowind/mods/46629) by RuffinVangarr  
Included and extended in NOD (both red and blue sets of armor are available now). Not gamebreaking to run together, but you'll have clones of the blue version of the armor, and two Ulains running around Hla Oad.
* [**More Argonian Hair**](https://www.nexusmods.com/morrowind/mods/43133) by ashiraniir  
Included in NOD, and even more Argonians given the new hairs. Incompatible because the NPC edits in the original will overwrite the more extensive outfit changes NOD makes.
* [**Hlaalu Nobles Facial Overhaul**](https://www.nexusmods.com/morrowind/mods/48916) by Leyawynn  
Included in NOD. Incompatible because the NPC edits in the original will overwrite the more extensive outfit changes NOD makes.
* [**Rogue's Gallery**](https://www.nexusmods.com/morrowind/mods/49874) by Von Djangos  
Included in NOD. Incompatible because the NPC edits in the original will overwrite the more extensive outfit changes NOD makes.
* [**OAAB data and Community Equipment Integration - RuffinVangarr Integrations**](https://www.nexusmods.com/morrowind/mods/50307) 
The RuffinVangarr integrations are included in NOD. Incompatible because the NPC edits in the original will overwrite the more extensive outfit changes NOD makes.

## Incompatible but patch available
None that I'm aware of for now.

## Known Incompatibilities
* [**Wares for NPCs**](https://www.nexusmods.com/morrowind/mods/52013) by Danae
Alternative outfit replacer. Use one or the other.
* [**Vanilla Friendly Wearables Expansion**](https://www.nexusmods.com/morrowind/mods/48683) by RandomPal
Alternative outfit replacer. Use one or the other.



# Recommended Mods
NOD doesn't cover everything. Here are some mods I recommend to fill in the gaps: they are fully compatible unless otherwise specified.

### General
* [**Weapon Sheathing**](https://www.nexusmods.com/morrowind/mods/46069) by Greatness7 et al
* [**Vanity**](https://www.nexusmods.com/morrowind/mods/48529) by Abot  
* [**Redoran War Armor and Sathil Mercenary Equipment**](https://www.nexusmods.com/morrowind/mods/50307) by Lucas92  
Requires the original mod by Ashtaar: [**Redoran War Armor and Sathil Mercenary Equipment**](https://www.nexusmods.com/morrowind/mods/44038). 
* [**Wandering Umbra**](https://www.nexusmods.com/morrowind/mods/44913) by Mort  
* [**Umbra - Blademaster**](https://www.nexusmods.com/morrowind/mods/43275) by Melchior Dahrk  
* [**The Raven**](https://www.nexusmods.com/morrowind/mods/21372) by Von Djangos, with the patch [**Sorkvild the Raven - Evermore**](https://www.nexusmods.com/morrowind/mods/46320?) by PoodleSandwich 
* [**Vampiric Bloodline Visages**](https://www.nexusmods.com/morrowind/mods/51201) by Stripes  
* [**Fancy Barenziah**](https://www.nexusmods.com/morrowind/mods/49009) by QwertyQuit  
* [**Mage Robes**](https://www.nexusmods.com/morrowind/mods/45739) by Melchior Dahrk
* IceNioliv Robe replacer - maybe be hard to find these days
* [**FMGS - Unique Items Compilation**](https://www.nexusmods.com/morrowind/mods/46433) by PoodleSandwich

### Guards
* [**Yet Another Guard Diversity**](https://www.nexusmods.com/morrowind/mods/45894) by Half11  
* [**Ruffin Vangarr YAGD Patch**](https://www.nexusmods.com/morrowind/mods/50307) by Lucas92
* [**Imperium - Legion Armor Expanded**](https://www.nexusmods.com/morrowind/mods/51408) by Endoran  
* [**RR Mod Series - Telvanni Cephalopod Armor**](https://www.nexusmods.com/morrowind/mods/44837) by Resdayn Revival Team  

## Morag Tong
* [**Morag Tong Helmet Diversity**](https://www.nexusmods.com/morrowind/mods/50738) by RuffinVangarr  
* [**MWSE - Morag Tong Helmets**](https://www.nexusmods.com/morrowind/mods/50827) by Stripes  
* [**Hein's Morag Tong Armors**](https://www.nexusmods.com/morrowind/mods/51144) by Heinrich and RuffinVangarr  

### Sixth House/Main Quest
* [**Dreamers Expansion**](https://www.nexusmods.com/morrowind/mods/42990) by Aoimevelho  
* [**Ashlander Rebels**](https://www.nexusmods.com/morrowind/mods/43225) by Aoimevelho  
* [**Dagoth Creatures Replacer**](https://www.nexusmods.com/morrowind/mods/42834) by Aoimevelho
* [**Ash Vampires Replacer**](https://www.nexusmods.com/morrowind/mods/42832) by Aoimevelho or [**Divine Dagoths**](https://www.nexusmods.com/morrowind/mods/45536) by SpaceDevo   
* [**Beware the Sixth House**](https://www.nexusmods.com/morrowind/mods/46036) by Mort
* [**Akulakhan's Best Chamber**](https://www.nexusmods.com/morrowind/mods/49644) by Duo Dinamico or [**Akulakhan Replacer**](https://www.nexusmods.com/morrowind/mods/42855) by Aoimevelho  

### Divinities
* [**By Azura**](https://www.nexusmods.com/morrowind/mods/50567) by Lamb Shark or [**Prince of Moonshadow - Azura Creature and Cinematic Replacer**](https://www.nexusmods.com/morrowind/mods/44492) by Saint Jiub   
* [**Almalexia Redone**](https://www.nexusmods.com/morrowind/mods/50265) by Lamb Shark
* [**Vivec Remade**](https://www.nexusmods.com/morrowind/mods/50317) by Lamb Shark or [**Divine Vivec**](https://www.nexusmods.com/morrowind/mods/46342) by SpaceDevo  



# FAQ
* Does this work on OpenMW/MWSE/vanilla Morrowind?
The main part of the mod should work on either OpenMW or a MWSE install, although I have only tested it with MWSE. Some outfits will not look correct without Morrowind Code Patch.

* Is this vanilla-friendly/lore-friendly?
I would describe NOD as Vanilla+++. It aims to add more colour and flair to NPC outfits, and overall has a sort of "magicpunk" vibe, similar to Investigations at Tel Eurus, Yul Marshee and the Visage of Mzund, or Expedition to Mzelthuand. Everything I have added has been carefully curated for balance and aesthetic - there should be nothing explicitly lore breaking, and in general I find that the new additions blend well once you get used to them. However, players who prefer a very purist aesthetic will probably not find it to their tastes.

* Does this give Caius a shirt?
What sort of monster do you think I am? No, he's safe. 

* Is this balanced?
Yes. I put a lot of effort into rebalancing and renaming items so that they fit in the vanilla namescheme and equipment progression curve. Some new pieces of clothing or armor are very strong (eg the Ceremonial Adamantium Armor is about 10% stronger than its vanilla equivalent), but nothing should be outrageously overpowered. If you find anything OP, please let me know and I'll fix it.

* Is this compatible with [x] mod?
Check the compatibility section. If it's not listed there, it should work with NOD. If it doesn't, let me know and I can either create a patch or list the incompatibility. In general, because NOD is an esm, it will load very early in your load order and therefore be compatible with most mods. Other mods that require NPC changes will either be patched by creating a merged objects file with tes3merge, or simply load later than NOD and 'win' the load order battle. In that case, you might miss out on some of the new outfits, but it's more important that eg quest mods are able to make their changes, since NOD is only cosmetic.

* Can you add [x] or remove [y] or change NPC [z] to the way I want them to be?
I am happy for you to make suggestions, as long as they are polite. However, this mod is designed to my personal tastes, because it's how I currently want to play the game, so I might not include your suggestion. The core mod file is an esm, so you can easily make an addon to change any NPC outfits you like, or to remove bits that you don't like. Another alternative for removing edits you don't like is to use tes3cmd.

* Can I make and release an addon/patch/fix?
Yes! Please do. Please see the Permissions section for more details.

* What's the difference between NOD and Wares for NPCs by Danae?
Primarily the difference is that NOD gives hundreds of NPCs unique and handcrafted outfits that remain consistent through each playthrough, whereas Wares for NPCs replaces *all* the clothes of *all* NPCs with leveled lists. Those leveled lists draw from any Wares-aware mods you have installed, meaning your game can look very different depending on your mod choices. The leveled lists are hand-tailored so that outfits mostly make sense and look good, however there is a lot of variability in how NPCs will look from game to game, and occasionally a complete fashion disaster.

tl;dr use NOD if you want handcrafted outfits, Wares for NPCs if you want something new every game.

* What's the difference between NOD and Vanilla Friendly Wearables Expansion by RandomPal?
NOD and VFWE are quite similar, and in fact VFWE was the primary inspiration for NOD. NOD is more extensive than VFWE in terms of both the raw number of NPC edits made (VFWE ~450, NOD ~800) and in the aesthetic changes that it makes. Also, NOD's documentation is much more granular - if you're worried about compatibility, it will be much easier to see which edits I've made. 

VFWE is, as the name implies, more vanilla friendly. NOD is more colourful and makes NPCs and cultural groups more distinct. VFWE includes many item replacers, whereas NOD focuses solely on NPCs and does not include item replacers. VFWE was built specifically to work with BCOM and you are likely to have errors if you do not also use BCOM alongside it. NOD was built without that requirement: it should work well with or without BCOM.

tl;dr Use NOD if you want more unique outfits, more color, don't use BCOM, or have your own item replacers in mind. Use VFWE if you want a BCOM-based game with a very vanilla-friendly aesthetic that also includes item replacers. 

* What's the best way to contact you?
Message me on Discord on the Morrowind Modding Community server (#Lucevar9271 - I have a Colovian Fur Helm avatar), or message me here on Nexus (Lucevar).



# Permissions
You are free to use anything that I, personally, have done. That means you can remix it, release patches, reupload this to another site if it becomes unavailable here on Nexus, include it in your own mod, or basically whatever you want to do as long as you are providing your mod for free and are not breaking Bethesda's terms of service or creating illegal content. You don't have to ask first. But please credit me, and do let me know - I'll want to check out your work!

As of version 1.0, "what Lucevar has done personally" is limited to the distribution choices (anything listed with a NOD: prefix in the NPC changelog), item renames and rebalances, and the MWSE scripts that distribute Fashionwind items 

PLEASE NOTE that that means that for a huge chunk of what's included in this mod, **IT IS NOT UP TO ME WHAT YOU CAN DO WITH IT**. If you wish to use the assets included in this mod, please refer to the original modder's permissions and wishes, and abide by those. I have included their original readmes in the archive. 

PLEASE ALSO NOTE I have done my best to get explicit permissions to use the mods included in NOD. Where it wasn't possible to get in touch with the original authors, I've done my best to check readmes and use only mods whose permissions allow it. If, despite that, for whatever reason, your mod is included here and you would rather I modify something or remove your assets, please reach out to me and I will do so.

In particular, many of the modders whose work I've included specify that anyone using their work **must not accept Nexus donation points**. As such, donation points will not be enabled on NOD, and I ask that you respect the wishes of the original authors as well.



# Credits
If I've accidentally left your name off this list, please get in touch and I'll update it asap. It wasn't intentional. 

In the /docs folder under 00 Core I've included the original readmes of all the mods included even partially. Please see the readmes for the full credit lists for the original mods.

In no particular order:
* RuffinVangarr (many mods, modeling advice)
* Leyawynn (Hlaalu Noble Facial Overhaul)
* Von Djangos (Rogues Gallery, hats from Properly Clothed NPCs)
* Lucas92 (OAAB and Community Equipment Integration)
* RandomPal (Properly Clothed NPCs and Netch Adamantium Integration)
Cythus, Jester
* Danae (Wares integrations, mesh and texture fixes, )
* Melchior Dahrk (MWSE scripts in Mage Robes)
* Westly
* Aoimevelho (Dunmer Nobles Overhaul, Buoyant Armigers Armor, Armored Robes, Dreamers Expansion)
* Plangkye (Hilgya the Seamstress)
* DimNussens (Dim's Khajiit Head and Hair Pack)
* Olaf 
* OAAB team
* TD team
* Ashiraniir (More Argonian Hair)
* Shehriazad (Redvayn's Humble Headgear)
* R-Zero (hat resources)
* Safebox - help and feedback, Onion - Layered Accessories
* TaiyakaJ - feedback and suggestions
* NullCascade (MWSE, CSSE, Mage Robes distribution code that I adapted for the Fashionwind addons)
* Hrnchamd - MGEXE and MCP and their various fixes
* Danke - Danke's armors
* Markond - Many Cloth Helms
* Korana - clothes used in the Streamer Safety addon