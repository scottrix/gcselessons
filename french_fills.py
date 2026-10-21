#!/usr/bin/env python3
"""French MFL theme fills: 5 theme dirs x 4 files (AQA-theme priority)."""
import re

def L(outcome, prior, link, analogy, vocab, we1, we2, errors, tip):
    return dict(outcome=outcome, prior=prior, link=link, analogy=analogy, vocab=vocab,
                we1=we1, we2=we2, errors=errors, tip=tip)

FRENCH = {}

# ============ customs-festivals ============
FRENCH["family-celebrations-1"] = L(
    "describe a family celebration in French using the passé composé and festive vocabulary",
    "free-time-activities (opinions and regular -er verbs)",
    "you'll reuse present-tense opinion phrases to say how you celebrated",
    "describing a birthday party — what happened, who was there, how it went",
    ["la fête (the party)", "les cadeaux (presents)", "le repas festif (festive meal)",
     "s'amuser (to have fun)", "le mariage (wedding)", "les fiançailles (engagement)"],
    {"q": "Décrivez une fête de famille récente. (4 marks)",
     "steps": "« L'année dernière, nous avons célébré les 60 ans de ma grand-mère. On a organisé une "
              "grande fête dans le jardin — il y avait trente invités ! J'ai offert un colis de chocolats "
              "français et j'ai fait un discours. C'était émouvant mais très amusant. »",
     "marks": "Passé composé ×3 (avoir), opinion + justification — the 4-mark structure"},
    {"q": "Quels sont les avantages et les inconvénients des grandes fêtes de famille ? (16 marks)",
     "steps": "P1 (avantages): « On voit toute la famille; les enfants s'amusent ensemble; c'est une "
              "tradition importante. » P2 (inconvénients): « C'est fatigant pour les parents; ça coûte "
              "cher; je préfère les petites fêtes. » Judgement: « Malgré le coût, je pense que les fêtes "
              "de famille sont essentielles. »",
     "complete": "Four-paragraph essay with two advantages, two disadvantages, and a justified conclusion."},
    [("« Les cadeaux » means the presents, not the cards — la carte is the card.",
      "Correct: les cadeaux = presents; les cartes de vœux = greeting cards"),
     ("Wrong: « j'ai amusé »", "Correct: « je me suis amusé(e) » — s'amuser is reflexive in the passé composé"),
     ("Wrong: « c'était très amusant » for a FUTURE party",
      "Correct: « ce sera très amusant » — future tense for future events")],
    "Name the celebration FIRST (« les 60 ans de ma grand-mère ») — specific detail earns communication marks."),
FRENCH["francophone-world-festivals-1"] = L(
    "describe a festival in the Francophone world and explain why it matters",
    "family-celebrations-1 (festive vocabulary and the passé composé)",
    "the same festive vocabulary describes both family parties and public festivals",
    "describing Glastonbury or Notting Hill Carnival — what happens, why people go, what makes it special",
    ["le festival (festival)", "le défilé (parade)", "la musique traditionnelle", "le carnaval (carnival)",
     "les danses folkloriques (folk dances)", "célèbre (famous)"],
    {"q": "Décrivez un festival dans le monde francophone. (4 marks)",
     "steps": "« Le Festival du Voyageur a lieu au Canada chaque février. Il y a des défilés, de la "
              "musique traditionnelle et des dégustations de sirop d'érable. C'est très célèbre au Manitoba. »",
     "marks": "Named festival + location + two activities + an opinion phrase"},
    {"q": "Pourquoi les festivals francophones sont-ils importants ? (16 marks)",
     "steps": "P1: « Les festivals gardent les traditions vivantes. » P2: « Ils attirent des touristes — "
              "bon pour l'économie locale. » P3: « Cependant, ils peuvent être bruyants et chers. » "
              "Judgement: « En général, ils renforcent la culture francophone. »",
     "complete": "Structured essay with a balanced argument and a justified conclusion."},
    [("« Le défilé » means the parade, not the delay — le retard is the delay.",
      "Correct: le défilé = parade; le retard = delay"),
     ("Wrong: « célébrer » without an object", "Correct: « célébrer QUELQUE CHOSE » — célébrer Noël, célébrer un anniversaire"),
     ("Wrong: « au Manitoba » written « à le Manitoba »",
      "Correct: « au Manitoba » — à + le contracts to au")],
    "Learn ONE festival in real detail (name, place, month, two activities) — exam questions reward specificity."),
FRENCH["major-french-festivals-1"] = L(
    "describe major French festivals using key dates and traditions",
    "francophone-world-festivals-1 (festival vocabulary)",
    "the same festival vocabulary transfers to French national celebrations",
    "describing Bonfire Night — a national event with food, fireworks and history",
    ["le 14 juillet (Bastille Day)", "Noël (Christmas)", "Pâques (Easter)", "le réveillon (Christmas Eve meal)",
     "les feux d'artifice (fireworks)", "la galette des Rois (Kings' cake)"],
    {"q": "Quelle est votre fête française préférée et pourquoi ? (4 marks)",
     "steps": "« Ma fête préférée, c'est le 14 juillet parce qu'il y a des feux d'artifice magnifiques et "
              "des défilés militaires. L'année dernière, j'ai regardé les feux d'artifice depuis la Tour "
              "Eiffel — c'était spectaculaire ! »",
     "marks": "Opinion + reason + a specific past example = 4 marks"},
    {"q": "Comparez deux fêtes françaises. (16 marks)",
     "steps": "P1 (Noël): « On échange des cadeaux et on mange le réveillon en famille. » "
              "P2 (14 juillet): « On regarde les feux d'artifice et on danse dans la rue. » "
              "P3 (comparison): « Noël est plus familial, mais le 14 juillet est plus festif. » "
              "Judgement: « Je préfère Noël parce que j'adore la cuisine de ma grand-mère. »",
     "complete": "Two festivals compared across food, atmosphere and family, with a justified preference."},
    [("« Le réveillon » is the MEAL, not the morning — le matin is the morning.",
      "Correct: le réveillon = the Christmas/New Year Eve feast"),
     ("Wrong: « la galette des Rois » eaten at Easter",
      "Correct: eaten on 6 January (Épiphanie) — know your festival dates"),
     ("Wrong: « les feux d'artifice » singular", "Correct: always plural — les feux d'artifice (the fireworks)")],
    "Dates in French: le 14 juillet (NOT le juillet 14) — day before month, always."),
FRENCH["regional-customs-and-traditions-1"] = L(
    "describe regional customs and traditions in France",
    "major-french-festivals-1 (national festival vocabulary)",
    "the same vocabulary describes local and regional celebrations",
    "describing a local festival in your town — what makes it different from national celebrations",
    ["la coutume (custom)", "la tradition (tradition)", "régional(e) (regional)", "le terroir (local heritage)",
     "le marché de Noël (Christmas market)", "la fête patronale (patron saint's festival)"],
    {"q": "Décrivez une coutume régionale française. (4 marks)",
     "steps": "« En Alsace, le marché de Noël de Strasbourg est très célèbre. Il ouvre fin novembre et il "
              "y a des chalets en bois, du vin chaud et des décorations artisanales. Ma famille y va chaque "
              "année. »",
     "marks": "Named region + custom + two details + a personal link"},
    {"q": "Les traditions régionales disparaissent-elles ? (16 marks)",
     "steps": "P1 (disparaissent): « Les jeunes quittent les villages; les supermarchés remplacent les "
              "produits locaux. » P2 (survivent): « Les marchés de Noël attirent plus de visiteurs chaque "
              "année; Internet fait connaître les traditions. » Judgement: « Elles changent, mais elles "
              "ne disparaissent pas. »",
     "complete": "Balanced argument with a nuanced conclusion — change is not the same as disappearance."},
    [("« La coutume » is feminine — « une coutume », not « un coutume ».",
      "Correct: une coutume régionale"),
     ("Wrong: « le terroir » = the earth", "Correct: le terroir = local land/heritage that gives food and "
      "wine their character"),
     ("Wrong: « chaque année » without « y » for 'there'", "Correct: « ma famille y va » — y replaces 'là-bas'")],
    "Pick ONE region (Alsace, Bretagne, Provence) and know its custom in detail — specificity beats breadth."),

# ============ free-time-activities ============
FRENCH["sports-and-hobbies-1"] = L(
    "talk about sports and hobbies using jouer à, faire de and opinions",
    "identity-relationships (present-tense -er verbs and opinions)",
    "you'll reuse present-tense verbs with new sport vocabulary",
    "talking about your weekly football match — when, where, who with, how often",
    ["jouer au foot (to play football)", "faire du vélo (to cycle)", "l'entraînement (training)",
     "une équipe (a team)", "s'entraîner (to train)", "le match (the match)"],
    {"q": "Qu'est-ce que tu fais comme sport ? (4 marks)",
     "steps": "« Je joue au football deux fois par semaine — mardi et samedi. Je fais aussi du vélo le "
              "dimanche avec mon père. Je m'entraîne sérieusement parce que je veux jouer en équipe "
              "première. »",
     "marks": "jouer à + faire de used correctly + frequency + justification"},
    {"q": "Les jeunes devraient-ils faire plus de sport ? (16 marks)",
     "steps": "P1 (pour): « Le sport est bon pour la santé et réduit le stress des examens. » "
              "P2 (contre): « Les devoirs sont plus importants; tout le monde n'aime pas la compétition. » "
              "P3 (alternatives): « On peut marcher ou danser au lieu des sports d'équipe. » "
              "Judgement: « Deux ou trois heures par semaine suffisent. »",
     "complete": "Balanced argument with a realistic, justified recommendation."},
    [("Wrong: « je joue du foot »", "Correct: « je joue AU foot » — jouer à for games/sports"),
     ("Wrong: « je fais le vélo »", "Correct: « je fais DU vélo » — faire de + du/de la/des"),
     ("Wrong: « je m'entraîne tous les jours » if you mean twice a week",
      "Correct: be accurate with frequency — deux fois par semaine")],
    "jouer à (games) vs faire de (activities) — learn three of each and never confuse them."),
FRENCH["music-and-cinema-1"] = L(
    "give opinions about music and cinema with justifications",
    "sports-and-hobbies-1 (opinion structures)",
    "the same opinion + justification structure transfers to music and film",
    "reviewing a film you saw last weekend — what, where, who with, verdict",
    ["le concert (concert)", "un film d'action (action film)", "le cinéma (cinema)",
     "les films d'horreur (horror films)", "j'adore / je déteste (I love / I hate)",
     "réalisé par (directed by)"],
    {"q": "Quel genre de musique aimes-tu ? (4 marks)",
     "steps": "« J'adore la musique rap française — j'écoute Stromae et PNL tous les jours. Je n'aime "
              "pas le classique parce que je le trouve ennuyeux. Mon groupe préféré, c'est... »",
     "marks": "Two opinions + justification + a named example"},
    {"q": "Décrivez le dernier film que vous avez vu. (16 marks)",
     "steps": "P1: « Le week-end dernier, je suis allé(e) au cinéma avec mes amis. » P2: « Nous avons vu "
              "un film d'aventures réalisé par... L'histoire se passe au Mexique. » P3: « Les effets "
              "spéciaux étaient incroyables mais le film était un peu trop long. » "
              "Judgement: « Je le recommanderais — 8 sur 10. »",
     "complete": "Past-tense narrative + detailed opinion + a rating — the 16-mark film review structure."},
    [("Wrong: « j'ai regardé un film au concert »",
      "Correct: film = au cinéma; concert = live music — don't swap the venues"),
     ("Wrong: « les films sont intéressant »", "Correct: « les films sont intéressantS » — plural agreement"),
     ("Wrong: « réalisé par » written « réalisé de »", "Correct: réalisé PAR + director's name")],
    "Past participles for cinema: vu (voir), aimé (aimer), trouvé (trouver) — three verbs cover most reviews."),
FRENCH["reading-and-technology-1"] = L(
    "talk about reading habits and technology use with frequency expressions",
    "music-and-cinema-1 (opinion vocabulary)",
    "the same opinion structures work for books, screens and apps",
    "explaining your screen-time habits — how often, what apps, why",
    ["la lecture (reading)", "un roman (a novel)", "la bande dessinée (comic)",
     "les écrans (screens)", "télécharger (to download)", "sur mon portable (on my phone)"],
    {"q": "Que fais-tu sur ton portable ? (4 marks)",
     "steps": "« Je passe environ deux heures par jour sur mon portable. Je regarde des vidéos, j'écoute "
              "de la musique et je télécharge des chansons. Je lis aussi des bandes dessinées sur mon "
              "appli de lecture. »",
     "marks": "Three activities + a frequency expression = full marks"},
    {"q": "La lecture papier ou numérique ? (16 marks)",
     "steps": "P1 (papier): « Les livres papier sont meilleurs pour les yeux et on se souvient mieux de "
              "l'histoire. » P2 (numérique): « C'est plus pratique — mille livres dans la poche! » "
              "P3 (compromise): « Je lis les deux selon la situation. » "
              "Judgement: « Malgré la technologie, je préfère les vrais livres. »",
     "complete": "Two-sided comparison with a personal verdict and a reason."},
    [("Wrong: « je lis sur le papier »", "Correct: « je lis des livres PAPIER » or « je lis en papier »"),
     ("Wrong: « la BD » for novels", "Correct: la BD = comic/bande dessinée; le roman = novel — don't confuse"),
     ("Wrong: « télécharger des livres » written with one d", "Correct: télécharger (two t's, two r's)")],
    "Frequency ladder: toujours > souvent > parfois > rarement > ne...jamais — know the order for listening."),
FRENCH["weekend-and-holiday-plans-1"] = L(
    "describe weekend and holiday plans using the near future (futur proche)",
    "reading-and-technology-1 (present tense + opinions)",
    "you'll reuse the present tense and add aller + infinitive for plans",
    "planning your weekend — what you're going to do, with whom, in what order",
    ["le week-end prochain (next weekend)", "les vacances (holidays)", "je vais + infinitif (I am going to...)",
     "on va + infinitif (we are going to...)", "d'abord, ensuite, enfin (first, then, finally)",
     "la plage (the beach)"],
    {"q": "Qu'est-ce que tu vas faire le week-end prochain ? (4 marks)",
     "steps": "« Le week-end prochain, je vais rendre visite à mes grands-parents. Samedi matin, on va "
              "faire les courses ensemble et l'après-midi, je vais réviser pour mes contrôles. Le soir, "
              "je vais me détendre avec un film. »",
     "marks": "Futur proche ×3 + sequencing words (d'abord, ensuite, enfin)"},
    {"q": "Où vas-tu passer tes prochaines vacances et pourquoi ? (16 marks)",
     "steps": "P1: « Cet été, je vais passer mes vacances dans le sud de la France. » P2: « On va louer "
              "un appartement près de la plage et on va faire de la planche à voile. » P3 (alternative): "
              "« Mes parents préfèrent la montagne, mais je vais gagner — j'espère! » "
              "Judgement: « Je pense que ce sera les meilleures vacances ever. »",
     "complete": "Near-future plans + a family disagreement + hope = the 16-mark holiday essay."},
    [("Wrong: « je vais à faire du sport »", "Correct: « je vais FAIRE du sport » — aller + infinitive, "
      "no preposition between them"),
     ("Wrong: « le weekend prochain, j'ai joué au foot » (for plans)",
      "Correct: future for plans — « je vais jouer » / « je jouerai »"),
     ("Wrong: « d'abord, ensuite, enfin » used randomly",
      "Correct: d'abord = first, ensuite = then, enfin = finally — keep the logical order")],
    "Sequencing words (d'abord, ensuite, enfin) are free structure marks — use all three in every 90-word answer."),

# ============ healthy-living ============
FRENCH["food-and-drink-1"] = L(
    "talk about food and drink using partitive articles (du, de la, des)",
    "weekend-and-holiday-plans-1 (present tense + frequency)",
    "you'll reuse present-tense verbs with partitive articles for food quantities",
    "describing what you eat for breakfast — quantities and preferences",
    ["le petit-déjeuner (breakfast)", "du pain (some bread)", "de la confiture (some jam)",
     "des céréales (some cereal)", "je mange / je bois (I eat / I drink)", "sain(e) (healthy)"],
    {"q": "Qu'est-ce que tu manges et bois d'habitude ? (4 marks)",
     "steps": "« D'habitude, au petit-déjeuner, je mange des céréales avec du lait et je bois un jus "
              "d'orange. À midi, je mange un sandwich au fromage et une pomme. Le soir, on mange "
              "ensemble en famille. »",
     "marks": "Partitive articles (du, de la, des) used correctly ×3 + meals named"},
    {"q": "Manger sainement, c'est important — ton avis ? (16 marks)",
     "steps": "P1: « Il faut manger cinq fruits et légumes par jour. » P2: « Mais la malbouffe est rapide "
              "et moins chère. » P3: « À mon avis, l'équilibre est plus important que l'interdiction. » "
              "Judgement: « Les écoles devraient offrir des menus sains gratuits. »",
     "complete": "Healthy-eating argument with school-policy recommendation — the 16-mark structure."},
    [("Wrong: « je mange du pomme »", "Correct: « je mange une pomme » or « des pommes » — pomme is feminine"),
     ("Wrong: « je bois le lait » (for a general habit)", "Correct: « je bois DU lait » — partitive for "
      "unspecified quantity"),
     ("Wrong: « le petit déjeuner » without the hyphen", "Correct: « le petit-déjeuner » — hyphenated")],
    "Après « je mange »: du (masculine), de la (feminine), des (plural) — three articles, three genders."),
FRENCH["healthy-lifestyle-choices-1"] = L(
    "discuss healthy lifestyle choices with il faut and_modal verbs",
    "food-and-drink-1 (food vocabulary + partitives)",
    "you'll reuse food vocabulary with il faut and devoir for advice",
    "giving advice to a friend who stays up late gaming — what they should change",
    ["il faut + infinitif (you must/it's necessary to)", "il vaut mieux (it's better to)",
     "dormir (to sleep)", "faire de l'exercice (to exercise)", "éviter (to avoid)",
     "le tabac (tobacco)"],
    {"q": "Que faut-il faire pour être en bonne santé ? (4 marks)",
     "steps": "« Il faut manger équilibré, dormir huit heures par nuit et faire de l'exercice "
              "régulièrement. Il vaut mieux éviter le tabac et limiter les écrans avant de dormir. »",
     "marks": "il faut + il vaut mieux + two specific recommendations"},
    {"q": "Les jeunes dorment-ils assez ? (16 marks)",
     "steps": "P1 (le problème): « Les écrans retardent le coucher; les devoirs finissent tard. » "
              "P2 (les effets): « La concentration baisse; le stress augmente. » "
              "P3 (les solutions): « Il faudrait limiter les écrans après 21 heures. » "
              "Judgement: « Les écoles devraient commencer plus tard! »",
     "complete": "Problem-effects-solutions structure with a policy recommendation."},
    [("Wrong: « il faut que tu dormir »", "Correct: « il faut dormir » — modal + infinitive, no conjugation"),
     ("Wrong: « je dois aller à la gym chaque jour » (overstating)",
      "Correct: be realistic — « trois fois par semaine » is more credible"),
     ("Wrong: « le tabac sont dangereux »", "Correct: « le tabac EST dangereux » — singular subject")],
    "il faut + INFINITIVE (no conjugation) — the easiest advice structure in French; use it three times."),
FRENCH["illness-and-injury-1"] = L(
    "describe illness and injury with avoir mal and body parts",
    "healthy-lifestyle-choices-1 (il faut + advice structures)",
    "you'll reuse il faut for health advice when describing symptoms",
    "explaining to a pharmacist that you hurt your ankle playing football",
    ["avoir mal à (to have a pain in)", "la tête (head)", "le genou (knee)", "la cheville (ankle)",
     "être malade (to be ill)", "se casser (to break)"],
    {"q": "Qu'est-ce qui ne va pas ? (4 marks)",
     "steps": "« Je ne me sens pas bien. J'ai mal à la gorge et j'ai de la fièvre depuis deux jours. "
              "Hier, je me suis cassé la cheville en jouant au foot — je dois voir le médecin. »",
     "marks": "avoir mal à + body part ×2 + a reflexive passé composé injury"},
    {"q": "Décrivez une fois où vous étiez malade. (16 marks)",
     "steps": "P1: « L'hiver dernier, j'ai attrapé une grippe terrible. » P2: « J'avais mal partout — "
              "la tête, le ventre, les muscles. Je ne pouvais pas aller au collège pendant une semaine. » "
              "P3 (résolution): « Ma mère a appelé le médecin; j'ai pris des médicaments et j'ai dormi. » "
              "Judgement: « Depuis, je me lave les mains tout le temps! »",
     "complete": "Past-tense illness narrative with body parts, duration and a lesson learned."},
    [("Wrong: « j'ai mal de la tête »", "Correct: « j'ai mal À LA tête » — toujours à + body part"),
     ("Wrong: « je suis cassé la jambe »", "Correct: « je me SUIS cassé la jambe » — reflexive + être"),
     ("Wrong: « le piedS »", "Correct: irregular plural — « les pieds » (one foot = le pied)")],
    "Body parts + avoir mal à: la tête, la gorge, le ventre, le dos, le genou, la cheville — six covers "
    "every exam role-play."),
FRENCH["mental-wellbeing-1"] = L(
    "discuss mental wellbeing and stress with emotional vocabulary",
    "illness-and-injury-1 (health vocabulary + advice)",
    "you'll reuse il faut and advice structures for mental-health recommendations",
    "advising a stressed friend before exams — what works for you",
    ["le stress (stress)", "se sentir (to feel)", "le bien-être (wellbeing)",
     "le buveur de café / fatigué(e) (tired)", "gérer (to manage)", "se détendre (to relax)"],
    {"q": "Comment te sens-tu avant les examens ? (4 marks)",
     "steps": "« Avant les examens, je me sens un peu stressé(e) mais je gère. Je me détends en écoutant "
              "de la musique et je fais du sport pour évacuer. Il est important de dormir aussi. »",
     "marks": "se sentir + two coping strategies + an opinion on sleep"},
    {"q": "Le bien-être des jeunes : les réseaux sociaux aident-ils ou nuisent-ils ? (16 marks)",
     "steps": "P1 (aident): « On reste en contact avec les amis; on trouve du soutien en ligne. » "
              "P2 (nuisent): « On compare sa vie aux autres; on dort moins. » "
              "P3 (nuancé): « Cela dépend de l'utilisation. » "
              "Judgement: « Il faut des limites de temps, pas une interdiction totale. »",
     "complete": "Balanced social-media debate with a policy conclusion — very current, very examinable."},
    [("Wrong: « je suis stressé tous les jours » (overstatement)",
      "Correct: « je suis parfois stressé(e) » — realism is more credible"),
     ("Wrong: « se détendre » conjugated as -er", "Correct: « je me détends » — reflexive -RE verb"),
     ("Wrong: « le bien-être » without the hyphen", "Correct: « le bien-être » — always hyphenated")],
    "Reflexive verbs for feelings: se sentir (to feel), se détendre (to relax), se reposer (to rest) — "
    "three cover most wellbeing answers."),

# ============ identity-relationships ============
FRENCH["personal-identity-1"] = L(
    "describe your personality and identity with adjective agreement",
    "healthy-living-1 (descriptions + advice)",
    "you'll reuse être + adjectives with correct agreement",
    "describing yourself for a new school — personality, qualities, what you're like",
    ["sociable (sociable)", "paresseux / paresseuse (lazy m/f)", "travailleur / travailleuse (hard-working)",
     "timide (shy)", "confiant(e) (confident)", "selon moi (in my opinion)"],
    {"q": "Comment décrirais-tu ta personnalité ? (4 marks)",
     "steps": "« Je suis plutôt sociable et confiant, mais un peu têtu! Mes amis disent que je suis "
              "travailleur parce que je révise tous les soirs. Ma sœur, elle, est plus timide que moi. »",
     "marks": "Four adjectives with correct agreement + a comparison"},
    {"q": "L'apparence est-elle importante pour l'identité ? (16 marks)",
     "steps": "P1 (pour): « Sur les réseaux sociaux, l'apparence compte beaucoup. » "
              "P2 (contre): « La personnalité dure plus longtemps que la beauté. » "
              "P3 (nuance): « Mais il ne faut pas ignorer la confiance en soi. » "
              "Judgement: « L'identité, c'est la personnalité + les passions, pas le miroir. »",
     "complete": "Social-media identity debate with a memorable conclusion."},
    [("Wrong: « je suis paresseuse » (said by a boy)", "Correct: « je suis paresseux » — masculine form"),
     ("Wrong: « mes amis dit que »", "Correct: « mes amis DISENT que » — -re verb plural"),
     ("Wrong: « selon moi, je pense que » (double)", "Correct: use ONE — « selon moi » or « je pense que »")],
    "Adjective agreement with je: add -e if you're female (paresseuse), keep masculine if male — know YOUR form."),
FRENCH["relationships-and-marriage-1"] = L(
    "discuss relationships and marriage with future and conditional",
    "personal-identity-1 (personality adjectives)",
    "you'll reuse adjective agreement and add future/conditional for plans",
    "talking about what kind of partner you'd like and whether you'll marry",
    ["le couple (couple)", "se marier (to get married)", "le mariage (marriage)",
     "divorcer (to divorce)", "fidèle (faithful)", "je voudrais (I would like)"],
    {"q": "Veux-tu te marier un jour ? (4 marks)",
     "steps": "« Oui, je voudrais me marier un jour — peut-être vers trente ans. Je cherche quelqu'un "
              "de fidèle et drôle. Mes parents sont mariés depuis vingt-cinq ans, donc je crois au "
              "mariage. »",
     "marks": "Conditional (je voudrais) + two qualities + a family example"},
    {"q": "Le mariage est-il démodé ? (16 marks)",
     "steps": "P1 (démodé): « Beaucoup de couples vivent ensemble sans se marier; le divorce est courant. » "
              "P2 (toujours pertinent): « Le mariage offre une sécurité légale et un engagement symbolique. » "
              "P3 (liberté): « Chacun doit choisir selon ses valeurs. » "
              "Judgement: « Ce n'est pas pour tout le monde, mais ce n'est pas démodé pour autant. »",
     "complete": "Balanced modern-relationships debate with a tolerant conclusion."},
    [("Wrong: « je voudrais me marier » conjugated in future",
      "Correct: je voudrais + INFINITIVE — conditional modal, no extra conjugation"),
     ("Wrong: « le mariage sont important »", "Correct: « le mariage EST important » — singular"),
     ("Wrong: « divorcer » confused with « se séparer »",
      "Correct: divorcer = legally divorce; se séparer = split up (not legal)")],
    "Conditional softens everything: je voudrais, je préférerais, ce serait — three verbs, instant "
    "top-band register."),
FRENCH["self-family-and-friends-1"] = L(
    "describe your family and friends with possessive adjectives",
    "relationships-and-marriage-1 (relationship vocabulary)",
    "you'll reuse relationship vocabulary with mon/ma/mes correctly",
    "introducing your family to a French exchange partner — who, ages, personalities",
    ["mon père / ma mère (my dad/mum)", "mes grands-parents (my grandparents)", "aîné(e) (eldest)",
     "cadet(te) (younger)", "mon meilleur ami (my best friend)", "proche (close)"],
    {"q": "Parle-moi de ta famille. (4 marks)",
     "steps": "« Dans ma famille, nous sommes cinq : mon père, ma mère, mes deux sœurs et moi. Je suis "
              "l'aîné(e). Ma grande sœur s'appelle Louise et elle est très drôle. Mon meilleur ami, "
              "c'est Thomas — on se connaît depuis la maternelle. »",
     "marks": "Family members + ages/order + a friend with a duration expression"},
    {"q": "Les amis sont-ils plus importants que la famille ? (16 marks)",
     "steps": "P1 (famille): « La famille est toujours là — même quand vous vous disputez. » "
              "P2 (amis): « Les amis vous CHOISISSENT — c'est différent. » "
              "P3 (les deux): « On a besoin des deux; ils ne remplacent pas l'un l'autre. » "
              "Judgement: « Pour moi, c'est égal — mais mes amis me comprennent mieux parfois. »",
     "complete": "Balanced family-vs-friends debate with a personal, nuanced conclusion."},
    [("Wrong: « mon sœur »", "Correct: « ma sœur » — sœur is feminine; the possessive agrees with the NOUN"),
     ("Wrong: « je suis le plus âgé » (for eldest girl)", "Correct: « je suis la plus âgée » — agreement"),
     ("Wrong: « depuis » with a past tense", "Correct: « je le connais DEPUIS cinq ans » + PRESENT tense")],
    "Possessives agree with the THING OWNED, not the owner: mon frère, ma mère, MES parents."),
FRENCH["social-issues-and-equality-1"] = L(
    "discuss social issues and equality with impersonal expressions",
    "self-family-and-friends-1 (family vocabulary)",
    "you'll reuse family vocabulary with il est important de + subjunctive triggers",
    "discussing homelessness and gender equality as you see them in your town",
    ["les sans-abri (homeless people)", "l'égalité (equality)", "la pauvreté (poverty)",
     "il est important de + inf (it's important to)", "la discrimination (discrimination)",
     "s'entraider (to help each other)"],
    {"q": "Quelles sont les grandes problèmes sociaux en France ? (4 marks)",
     "steps": "« Il y a plusieurs problèmes : la pauvreté, le chômage des jeunes et la discrimination. "
              "Il est important d'en parler et de s'entraider. Chez moi, je vois des sans-abri dans le "
              "centre-ville. »",
     "marks": "Three named issues + an impersonal opinion + a local example"},
    {"q": "L'égalité entre les hommes et les femmes est-elle atteinte ? (16 marks)",
     "steps": "P1 (progrès): « Les femmes travaillent et étudient comme les hommes maintenant. » "
              "P2 (inégalités): « Mais les salaires ne sont pas égaux et les tâches ménagères restent "
              "inégales. » P3 (solutions): « L'éducation est la clé; les lois aident aussi. » "
              "Judgement: « On progresse, mais le combat continue. »",
     "complete": "Progress-inequality-solutions structure with a forward-looking conclusion."},
    [("Wrong: « les sans-abri est pauvre »", "Correct: « les sans-abri SONT pauvres » — plural"),
     ("Wrong: « il est important de parlant »", "Correct: « il est important de PARLER » — de + infinitive"),
     ("Wrong: « la discrimination contre les femmes » written « de »",
      "Correct: discrimination CONTRE + group")],
    "Impersonal opinion phrases: il est important de / il faut / il vaut mieux — three openers, endless "
    "essays."),

# ============ travel-tourism ============
FRENCH["travel-and-transport-1"] = L(
    "discuss travel and transport with en and prepositions of transport",
    "identity-relationships-1 (social issues + impersonal phrases)",
    "you'll reuse impersonal phrases to compare transport options",
    "explaining how you get to school and why — bus, bike, walking",
    ["en train (by train)", "en avion (by plane)", "à vélo (by bike)", "à pied (on foot)",
     "le billet (ticket)", "le quai (platform)"],
    {"q": "Comment voyages-tu d'habitude ? (4 marks)",
     "steps": "« D'habitude, je vais au collège à pied — c'est à dix minutes. Pour les vacances, nous "
              "voyageons en train parce que c'est plus écologique que l'avion. J'adore regarder le "
              "paysage par la fenêtre. »",
     "marks": "Three transport prepositions used correctly (à pied, en train) + a reason"},
    {"q": "L'avion est-il le pire choix pour la planète ? (16 marks)",
     "steps": "P1 (oui): « L'avion pollue dix fois plus que le train. » P2 (nuance): « Mais pour les "
              "longues distances, il n'y a pas d'alternative. » P3 (solutions): « Le train pour "
              "l'Europe; moins de vols courts. » Judgement: « Il faut changer nos habitudes. »",
     "complete": "Environmental transport debate with concrete alternatives."},
    [("Wrong: « je voyage en pied »", "Correct: « je vais À PIED » — à pied, not en pied"),
     ("Wrong: « en le train »", "Correct: « EN train » — no article after en for transport"),
     ("Wrong: « le billet » and « le ticket » confused", "Correct: le billet = train/plane; le ticket "
      "= bus/metro/local")],
    "Transport prepositions: EN (train, avion, voiture) vs À (vélo, pied, cheval) — two lists, never mixed."),
FRENCH["holiday-preferences-1"] = L(
    "compare holiday preferences with comparatives and superlatives",
    "travel-and-transport-1 (transport prepositions)",
    "you'll reuse transport vocabulary with plus/moins/aussi comparisons",
    "arguing beach vs mountain holidays with your family",
    ["la mer (the sea)", "la montagne (the mountains)", "le camping (camping)",
     "l'hôtel (hotel)", "la plage (beach)", "je préfère (I prefer)"],
    {"q": "Tu préfères les vacances à la mer ou à la montagne ? (4 marks)",
     "steps": "« Je préfère les vacances à la mer parce que j'adore nager et faire de la planche à "
              "voile. La montagne, c'est beau, mais il fait plus froid et il y a moins d'activités "
              "aquatiques. Ma sœur, elle, préfère la montagne — elle fait de la randonnée. »",
     "marks": "Comparative (plus/moins) + two preferences + a family contrast"},
    {"q": "Les vacances idéales : hôtel ou camping ? (16 marks)",
     "steps": "P1 (hôtel): « Le confort, la piscine, le petit-déjeuner inclus. » P2 (camping): "
              "« La nature, l'aventure, c'est moins cher. » P3: « Mais la pluie sous une tente, "
              "c'est le pire! » Judgement: « Le camping en été, l'hôtel en hiver — le meilleur des "
              "deux mondes. »",
     "complete": "Accommodation comparison with a seasonal compromise."},
    [("Wrong: « la mer est plus mieux »", "Correct: « la mer est MEILLEURE » — meilleur for nouns, "
      "mieux for verbs"),
     ("Wrong: « le camping est moins cher QUE au camping? »", "Correct: « moins cher que l'hôtel » — "
      "compare like with like"),
     ("Wrong: « je préfère l'hôtel que le camping »", "Correct: « je préfère l'hôtel AU camping » — "
      "préférer takes à/de, not que")],
    "préférer + À (not que); comparatives use plus/moins/aussi ... QUE — two structures, don't mix."),
FRENCH["accommodation-and-booking-1"] = L(
    "book accommodation and solve problems with polite requests",
    "holiday-preferences-1 (holiday preferences + comparisons)",
    "you'll reuse preference vocabulary for booking interactions",
    "calling a hotel to change a booking — polite requests, dates, problems",
    ["une chambre double (a double room)", "réserver (to book)", "la réservation (booking)",
     "complet(e) (full)", "la nuit (night)", "je voudrais réserver (I'd like to book)"],
    {"q": "Réservez une chambre au téléphone (role-play). (4 marks)",
     "steps": "« Bonjour, je voudrais réserver une chambre double pour deux nuits, du 12 au 14 août. "
              "C'est possible ? ... Avec vue sur la mer, si possible. Le petit-déjeuner est-il inclus ? »",
     "marks": "je voudrais + room type + dates + a polite question"},
    {"q": "Décrivez un problème de voyage et comment vous l'avez résolu. (16 marks)",
     "steps": "P1 (le problème): « L'été dernier, notre hôtel était complet — la réservation avait "
              "disparu! » P2 (les solutions): « On a cherché un autre hôtel en ligne; on a fini par "
              "trouver une chambre. » P3 (leçon): « Depuis, je confirme toujours par e-mail. » "
              "Judgement: « Les problèmes de voyage sont inévitables — l'important est de rester calme. »",
     "complete": "Problem-solution-lesson narrative — the 16-mark travel story."},
    [("Wrong: « une chambre pour deux personnes » = « une chambre double »? ",
      "Correct: chambre double = double bed; chambre twin = two beds — know the difference"),
     ("Wrong: « du 12 au 14 août » written « de 12 à 14 août »",
      "Correct: du... au... — de + le contracts"),
     ("Wrong: « il est complet » for a room", "Correct: « l'hôtel est complet » — the HOTEL is full, "
      "not the room")],
    "Role-play formula: greeting + je voudrais + specifics (dates/room) + one polite question."),
FRENCH["tourist-situations-and-problems-1"] = L(
    "handle tourist problems with past-tense narratives and solutions",
    "accommodation-and-booking-1 (booking vocabulary)",
    "you'll reuse booking vocabulary with passé composé problem narratives",
    "lost passport, stolen bag, missed train — telling a travel disaster story",
    ["le passeport perdu (lost passport)", "le vol (theft/flight)", "la gare (station)",
     "perdre (to lose)", "se faire voler (to have stolen)", "la police (police)"],
    {"q": "Qu'est-ce qui s'est passé pendant tes vacances ? (4 marks)",
     "steps": "« Le premier jour, je me suis fait voler mon sac à la gare! J'ai perdu mon passeport et "
              "mon argent. Je suis allé(e) au commissariat et j'ai fait une déclaration. Heureusement, "
              "mes parents ont eu une copie du passeport. »",
     "marks": "se faire voler + perdre + PC ×3 + a resolution"},
    {"q": "Les touristes sont-ils des cibles faciles ? (16 marks)",
     "steps": "P1 (oui): « Les touristes portent des objets chers et ne connaissent pas la ville. » "
              "P2 (conseils): « Il faut faire attention, garder les copies et éviter les endroits "
              "isolés. » P3 (contre): « Mais la plupart des voyages se passent sans problème. » "
              "Judgement: « Un peu de prudence suffit. »",
     "complete": "Risk-assessment essay with practical advice and a reassuring conclusion."},
    [("Wrong: « j'ai volé mon sac » (you stole it?!)", "Correct: « ON M'A volé mon sac » or « je me "
      "suis fait voler » — passive/reflexive for being robbed"),
     ("Wrong: « le vol » always means theft", "Correct: le vol = theft OR flight — context decides"),
     ("Wrong: « à la gare, je perds mon passeport » (present for past)",
      "Correct: « j'ai PERDU mon passeport » — past event, past tense")],
    "se faire + infinitif = to have something done TO you — se faire voler, se faire attaquer."),
