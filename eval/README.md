# Output Examples

We choose 12 languages based on the coverage of LLaMA and Bloom during pretrain. 
And randomly choose a question and outputs (from different model) for each language.
The question set is sampled from [FastChat Eval Set](https://github.com/lm-sys/FastChat/blob/main/fastchat/eval/table/question.jsonl) and translated into a target language use Google Cloud Translation.

Templates for different models are listed below.
```json
{
    "description": "Template of Bactrian-Bloom, Bactrian-LLaMA.",
    "prompt_no_input": "### Input:\n{Question}\n\n### Output:\n",
    "response_split": "### Output:\n"    
}
```

```json
{
    "description": "Template of Bloom, Bloomz No Prompt.",
    "prompt_no_input": "{Question}\n\n",
    "response_split": "\n\n"    
}
```

```json
{
    "description": "Template of Bloomz Alpaca Prompt, Alpaca.",
    "prompt_no_input": "Below is an instruction that describes a task. Write a response in {Language} that appropriately completes the request.\n\n### Instruction:\n{Question}\n\n### Response:\n",
    "response_split": "### Response:\n"    
}
```

For better display, we set a cutoff length for each answer to 256 characters.

### Languages both LLaMA and Bloom covered in pretrain.

#### Spanish
```json
{
"Question": "¿Cuáles son los factores principales que influyen en el comportamiento del consumidor?",
"Bactrian-Bloom": "Los factores principales del comportamiento del consumo incluyen:\n\n1. La cultura y la sociedad: La cultura, la sociedad y la economía influyen significativamente en el consumo de los consumidores. Por ejemplo, en países con una cultura de consumo más alta,",
"Bactrian-LLaMA": "Los factores más importantes que influyan en el consumo del consumidores son:\n\n1. Precio: el precio es un factor clave para el consumidor, ya que influye en la decisión de comprar o no un producto.\n\n2. Calidad: la calidad es otro factor importante para el ",
"Bloom": "El comportamiento del comprador es un proceso complejo que se ve influido por muchos factores.\nEntre ellos se encuentran los siguientes:\n\na) Factores económicos:\n\ni) El nivel de ingresos de la familia;\n\nii) El tipo de empleo;\n\niii) El número de miembros de",
"Bloomz No Prompt": "El comportamiento del cliente se ve afectado por factores psicológicos, sociales, culturales, económicos y políticos.</s>",
"Bloomz Alpaca Prompt": "El precio, la calidad, la conveniencia, la disponibilidad, la marca, la publicidad, la recomendación, la experiencia, la personalidad, la cultura, la religión, la edad, el género, la ubicación, la situación familiar, la salud, la educación, la ocupación, l",
"Alpaca": "Los factores más importantes que influye en el consumidor son el precio, la calidad, la disponibilidad, el marketing, la experiencia del consumo, la opinión de los amigos y familiares, la seguridad financiera, la cultura y la experieniencia del consumidore"
}
```

```json
{
"Question": "Como colonista del espacio en Marte, describa su vida diaria y los desafíos que enfrenta vivir en otro planeta.",
"Bactrian-Bloom": "Mi vida diaria en Marte es bastante similar a la de cualquier otra persona en la Tierra. Tengo acceso a la misma tecnología y recursos que cualquier otra civilización en la tierra, pero la vida en Marte también tiene sus desafíos.\n\nEn primer lugar, la grav",
"Bactrian-LLaMA": "Desafío 1: Adaptación a la vida en MarTE\n\nComenzando con la adaptación a una vida en el espacio, es importante tener en cuenta que la vida no es la misma en MarTÉ como en la Tierra. La presión atmosférica es menor, la gravedad es menor y la temperatura es ",
"Bloom": "El Sr.\nKennedy (Estados Unidos de América) dice que la exploración espacial es una actividad de interés público que tiene por objeto mejorar la calidad de vida de la humanidad.\nLa exploración espacial ha permitido a la humanidad conocer mejor el universo y",
"Bloomz No Prompt": "The Mars colonist, describe his daily life and the challenges he faces living on another planet.</s>",
"Bloomz Alpaca Prompt": "En Marte, la vida es dura. Los colonizadores deben lidiar con el clima extremo, la falta de agua y la falta del aire.</s>",
"Alpaca": "As a colonist on Mars, my daily life is filled with challenges and adventures. I wake up early in the morning to prepare for the day ahead. I take a shower, eat breakfast, and get ready for work. I spend my days working on projects, exploring the planet, a"
}
```


#### French
```json
{
"Question": "Comment les obstacles linguistiques et culturels affectent-ils la façon dont les gens communiquent et nouent les relations dans les sociétés multiculturelles?",
"Bactrian-Bloom": "Les obstacles linguistiques peuvent avoir un impact significatif sur la façon de communiquer et de nouer des relations dans une société multiculturelle. Les différences culturelles peuvent également avoir un effet sur la communication, car les gens peuvent",
"Bactrian-LLaMA": "Les obstacles langagiers et culturellement divers peuvent avoir un impact significatif sur la façade de communication et la formation de relations dans des sociétés multi-culturelles. Les langues et les cultures peuvent être des obstacles à la compréhensio",
"Bloom": "Comment les médias peuvent-ils contribuer à la compréhension et à la tolérance entre les peuples?\n\nComment la société civile peut-elle contribuer à promouvoir la compréhension, la tolérance et la solidarité entre les cultures?\n\nComment le dialogue intercul",
"Bloomz No Prompt": "Les obstacles linguistiques affectent la façon de communiquer et de nouer des relations dans des sociétés multiraciales.</s>",
"Bloomz Alpaca Prompt": "Les obstacles linguistiques affectent la façon de communiquer et de nouer des relations dans des sociétés multiraciales.</s>",
"Alpaca": "The linguistic and cultural obstacles can affect the way people communicate and form relationships in multicultural societies. Language barriers can prevent people from understanding each other, while cultural differences can lead to misunderstandings and "
}
```

```json
{
"Question": "Quels facteurs envisageriez-vous lors de la conception d'un système de transport public inclusif et accessible?",
"Bactrian-Bloom": "En tant qu'IA, je n'ai pas de préférence personnelle, mais voici quelques facteurs à considérer lors de l'élaboration d'un système inclusif de transport public:\n\n1. Accessibilité physique: Les systèmes de transport doivent être accessibles aux personnes ha",
"Bactrian-LLaMA": "1. Accessibilité : le système de transports inclusif doit être accessible à tous les usagers, y compris les personnes handicapées, les personnes âgées et les personnes à mobilité réduite.\n\n2. Accessiblité des stations : les stations de transit doivent être",
"Bloom": "M. K. S. Saha (Inde) dit que les transports publics sont un élément essentiel de la mobilité urbaine et que les systèmes de transport inclusifs et accessibles sont un moyen de réduire la pauvreté et d'améliorer la qualité de vie.\nLes transports publics inc",
"Bloomz No Prompt": "Accessibilité</s>",
"Bloomz Alpaca Prompt": "Accessibilité physique, accessibilité économique, accessibilités sociales et culturelles, accessibillité politique, accessibiité cognitive, accessiblité physique,</s>",
"Alpaca": "When designing a public transport system that is inclusive and accessible, I would consider factors such as accessibility for people with disabilities, the availability of accessible transportation, the cost of transportation and the ease of use of the sys"
}
```


#### Portuguese
```json
{
"Question": "Como a linguagem e as barreiras culturais afetam a maneira como as pessoas se comunicam e formam relacionamentos nas sociedades multiculturais?",
"Bactrian-Bloom": "A linguagem e a cultura são duas áreas que afetam significativamente a maneira com que as pessoas comunicam-se e formam relações nas sociedades multiculturales. A linguagem é um meio de comunicação que permite que as culturas se comuniquem e se entendam. A",
"Bactrian-LLaMA": "A linguagem é um dos principais fatores que afetem a manutenção de relacionamentos e a comunicação entre as pessoa em sociedade multicultural. A linguagem pode ser uma barreira significativa para as pessoais que não falam a língua dominante da sociedede. A",
"Bloom": "Como a globalização e a tecnologia afetam as culturas e as identidades culturais?\n\nComo as culturas se relacionam com a economia e a política?\n\nComo os valores culturais se relacionaram com a história e a sociedade?\n\nComo o desenvolvimento econômico e a gl",
"Bloomz No Prompt": "Yes</s>",
"Bloomz Alpaca Prompt": "A linguagem e a cultura são fatores importantes na comunicação e na formação de relacionamentos.</s>",
"Alpaca": "A linguagem é uma das principais barreira culturales que afetamos a maner como as personas se comuniquen e formen relacionamentos nos sociedade multicultural. A linguagem serve como um mecanismo para identificar e distinguir as diferentes culturas, e por i"
}
```

```json
{
"Question": "Como os governos podem utilizar políticas fiscais e monetárias para combater as recessões econômicas?",
"Bactrian-Bloom": "Os governos podem usar políticas fiscais, monetárias e de regulação para combater recessões económicas. As políticas fiscais incluem impostos, subsídios e gastos governamentais. As medidas monetárias incluem a taxa de juros, a quantidade de dinheiro em cir",
"Bactrian-LLaMA": "Os governos têm várias opções para combate a recessão econônica, incluindo políticas de fiscal e monetal. Aqui estão algumas opções:\n\nPolíticas fisicais:\n- Redução de impostos: os governantes podem reduzir os impostores para incentivar a compra de bens e s",
"Bloom": "A política fiscal pode ser utilizada para combater a recessão econômica, mas não é a única política que pode ser usada. A política monetária também pode ser empregada para combater uma recessão. A inflação pode ser reduzida, o que pode reduzir o custo do d",
"Bloomz No Prompt": "Yes</s>",
"Bloomz Alpaca Prompt": "Aumento de impostos e redução de gastos</s>",
"Alpaca": "Os governos usam políticas fiscárias e monetaires para combate as recesões económicas. As políticas monetarias incluem a redução da taxa de juros, a reducao da taxas de transferência e a reduçao das taxas bancárias. As polícias fiscaíres incluem reduções n"
}
```

### Languages Bloom covered but LLaMA not covered in pretrain.

#### Arabic
```json
{
"Question": "ما هي الاختلافات بين مصادر البروتين النباتية والحيوانية؟",
"Bactrian-Bloom": "1- مصادر البروتين:\n- مصادر البروتينات الحيوانية: اللحوم، الأسماك، البيض، الحليب، الجبن، الزبادي، اللحوم الحمراء، الدجاج، الخنزير، الخ.\n- مصادر بروتين النباتية: الحبوب، المكسرات، الفواكه، الخضروات، الحبوب الكاملة، المكملات الغذائية.\n\n2- القيمة الغذائية:\n- ا",
"Bactrian-LLaMA": "1- تناول البيئة: يتم توفير المصدرات البشرية الناتجة من البناء البسيط وتحويلها إلى مواد غذائية. بالمقارنة ، يحتوي المورد البصير على البواسطة الباردة للبياناسي ويتولىه البحر ولا يستخدم بعض المناطق البلادية، وهو يعمل عن طريق تحمل الماء مع الأرض وإنتاج البقالة",
"Bloom": "الاختلافات الرئيسية بين مصادر بروتين النبات والحيوان هي:\n\n1 - محتوى البروتين\n\nيحتوي البروتين على الأحماض الأمينية الأساسية التي يحتاجها الجسم، والتي لا يمكن أن يصنعها الجسم من تلقاء نفسه.\nوتعتبر اللحوم والدواجن والأسماك من المصادر الغنية بالبروتين، ولكن يج",
"Bloomz No Prompt": "تختلف مصادر البروتينات النباتية عن مصادر البروتينية الحيوانية في عدة جوانب:</s>",
"Bloomz Alpaca Prompt": "تختلف مصادر البروتينات النباتية عن مصادر البروتينية الحيوانية في عدة جوانب.</s>",
"Alpaca": "الاخلاقات التي يتم تقييمها باستخدام المصلحة المياهية التى تمثل بريتانا في مجال البيئة من خلال تحميل الباروينيات، وهي تعمل على اساس التمكين، انهاء التراكم وتمييز الموارد بالتماري واسمع عن اي اخر موضوع مثيل للتمرير ولا يمكن له احتاج لمصالحة تجاهل مايسمان بعض"
}
```

```json
{
"Question": "ما هي الطرق الأكثر فعالية للتعامل مع التوتر؟",
"Bactrian-Bloom": "هناك العديد من الطرق الفعالة للتعامل والتخفيف من التوتر، ومنها:\n\n1- ممارسة الرياضة: تساعد الرياضة على تحسين المزاج وزيادة الطاقة، كما أنها تساعد على تقليل التوتر.\n\n2- الاسترخاء والتنفس العميق: يمكن استخدام الاسترخاء للتخلص من التوتر والتوتر، حيث يمكن ممارس",
"Bactrian-LLaMA": "1- التفكير الإيجابي: يمكن لمن يعمل التعلم عن التحديات والتواصل بشكل إيقافي من المشاكل المحتملة وتحسين النمط الحيائي ومنع الانتهاء ممارسة التركيز على الموضوع المعين.\n\n2- الاسترخاء: تستخدم المناسبات الرياضية المثل الركوب و التماسيح و تم تحضير مواقف متنوعة مث",
"Bloom": "إنني أؤيد تماما ما قاله السفير فييت نام.\nإننا نؤيد أيضا ما قاله ممثل ألمانيا.\nإنني أعتقد أن هناك حاجة إلى مزيد من العمل في هذا المجال.\nإن هناك حاجة أيضا إلى مزيد العمل في مجال بناء القدرات.\nإن بناء القدرات هو أمر حيوي.\nإن هذا هو السبب في أننا نرحب بالجهود ",
"Bloomz No Prompt": "يمكن أن تساعدك بعض الطرق التالية على التعامل مع التوتر:\n\nالتأمل\n\nالتدليك\n\nالتمارين الرياضية\n\nالاسترخاء\n\nالتغذية السليمة</s>",
"Bloomz Alpaca Prompt": "تناول الطعام الصحي، ممارسة الرياضة، النوم الجيد، وتجنب المخدرات والكحوليات.</s>",
"Alpaca": "التعليم والتدريب هم أيضا من الطلاقات الأفضل لتقديم العمليات وتعميل المواقع المحلية."
}
```


#### Indonesian
```json
{
"Question": "Bagaimana Anda memperkenalkan diri sebagai ksatria abad pertengahan di jamuan kerajaan?",
"Bactrian-Bloom": "Saya adalah ksatri abad pertengahan yang sangat bangga dan terhormat. Saya sangat senang bisa hadir di jamuannya kerajaan dan berharap dapat memberikan kontribusi yang positif bagi acara ini. Saya juga sangat senang bertemu dengan para tamu undangan yang t",
"Bactrian-LLaMA": "Saya, sebagian dari ksatriya abad pertama, mempertimbangkan bagaimannya dalam kerajaannya. Saya memperhatikan bagaimanapun, ksatraja yang saya pikirkan adalah seorang pria yang sangat kuat dan kuas. Dia memiliki kekuasaan yang luas dan dapat menghadapi sem",
"Bloom": "A:\n\nSaya tidak tahu apakah ini benar, tapi saya pernah membaca bahwa seorang ksatri abad pertengahan tidak akan memperkenalkan diri dengan nama aslinya, tapi dengan nama yang lebih sopan. Misalnya, jika ia bernama John, ia akan memperkenalkan dirinya sebag",
"Bloomz No Prompt": "The way you introduce yourself as a medieval knight at a court feast</s>",
"Bloomz Alpaca Prompt": "Saya adalah ksatrian abad pertengahan dari kerajaan Inggris.</s>",
"Alpaca": "Anda harus mempertimbangkan diri untuk menjadi ksatriya abad pertama di jamu abad. Anda haruskah memperkentangkan kepentingan dan kepribadian diri dengan kependayan dan pengamatan. Andakan haruskaha memperkecualikan diri dalam kepercayaan dan keperawatan."
}
```

```json
{
"Question": "Apa saja implikasi potensial menggunakan botol plastik sekali pakai versus botol yang dapat digunakan kembali pada lingkungan dan kesehatan manusia?",
"Bactrian-Bloom": "Implikasi potensial dari penggunaan botol plastik yang sekali pakai pada lingkungan adalah sebagai berikut:\n\n1. Meningkatkan jumlah sampah plastik di lingkungan, yang dapat menyebabkan kerusakan pada ekosistem dan hewan-hewan yang bergantung pada plastik.\n",
"Bactrian-LLaMA": "1. Kesehatannya: Botol plastic yang digunai sekala pakai dapat menyebabkan penyakit kronis seperti penyebaran kanker, penyembuhan kankeras, dan penyumbatan kankerserumah.\n\n2. Lingkungannya dan Kesejahteraan: Botolan plastikan dapat bertumbuh dan bertahan l",
"Bloom": "1. Botol plastik sekali gunakan\n\nBotol plastik yang digunakan sekali pakai adalah botol yang tidak dapat digunakan lagi setelah digunakan. Botolan plastik yang tidak bisa digunakan lagi ini biasanya terbuat dari bahan plastik yang mudah rusak, seperti plas",
"Bloomz No Prompt": "Bahan plastik yang digunakan untuk membuat botol sekali pakai tidak dapat didaur ulang dan tidak dapat diproses menjadi bahan bakar. Botol sekali pakai juga tidak dapat disterilkan dengan cara yang sama seperti botol yang bisa digunakan kembali.</s>",
"Bloomz Alpaca Prompt": "Bahan plastik yang digunakan untuk membuat botol sekali pakai tidak dapat terurai dengan baik. Botol sekali pakai dapat menyebabkan polusi air dan tanah. Botolan sekali pakai juga dapat menyebabkan kerusakan pada kesehatan manusia.</s>",
"Alpaca": "The potential implications of using plastic bottles versus reusable bottles in the environment and health of humans include:\n\n1. Plastic bottle production requires large amounts of energy and water, and releases large amounts carbon dioxide and other green"
}
```


#### Chinese
```json
{
"Question": "假装是世界末日世界中的角色。描述您如何生存和遇到的盟友。",
"Bactrian-Bloom": "作为AI，我没有情感和身体，因此无法生存。但是，我可以想象一个世界末日世界，其中角色们需要面对各种挑战和威胁。\n\n首先，角色们必须找到食物和水，因为没有这些资源，他们就无法生存。他们可以寻找一些可以吃的东西，例如动物尸体、腐烂的植物等。他们还可以寻找一些水，例如河流、湖泊等。\n\n其次，角色需要寻找庇护所，因为世界末日可能会导致许多地方被摧毁，例如房屋、建筑物等。角色们可以寻找一个安全的空间，例如洞穴、山洞等。此外，角色还可以寻找盟友，例如其他角色、动物等。这些盟友可以帮助他们找到食物、水和庇护所。\n\n最后，",
"Bactrian-LLaMA": "我是一名人物，在世界的朕朦中生存。我的身体是强壮的，可以快速逃脱危险的环境。我能够吃食物，温暖和保持身体的渴望。我还能听到和理解语言，从而与人们交流。\n我的精神和智力也很強，我能理解和解决各种问题。\n在我的旅程中，我遭遗着吸引人的卫星和宇宙船。我也遢到了一些即将恢复的城市，寻找了终结的世界。\n最绫，我的生存方式是一种充满冒険和挑战的生活。我往待睡眠，忍耐督走，尝试寓意和感受，以探索世界和自己的生命。.",
"Bloom": "在我们的日常生活中，我们经常会遇到一些问题，比如：我们经常在电视上看到一些关于火灾的新闻，火灾的危害非常大，所以我们必须注意防火。那么，在我们的生活中，我们如何预防火灾呢？下面，让我们来看看防火涂料厂家介绍的防火涂料的防火原理。</s>",
"Bloomz No Prompt": "If you are a female, describe how you are treated by the male characters.</s>",
"Bloomz Alpaca Prompt": "我是一名士兵，我生活在废墟中。我遇到了一个女孩，她帮助了我。</s>",
"Alpaca": "I am the last character in the world. I describe how I survive and meet friends."
}
```

```json
{
"Question": "语言和文化障碍如何影响人们在多元文化社会中交流和建立关系的方式？",
"Bactrian-Bloom": "在多元文化的背景下，语言和文化的障碍可能会影响人们交流和沟通的方式。以下是一些例子：\n\n1. 语言障碍：人们可能无法理解或表达自己想要表达的意思，这可能会导致误解和冲突。\n\n2. 文化障碍：不同文化背景的人可能会有不同的价值观和行为方式，这可能导致沟通和理解上的困难。\n\n3. 偏见和文化歧视：人们可能会基于文化、种族、性别、年龄等原因而产生偏见和文化偏见，这可能阻碍人们建立关系和交流。\n\n4. 沟通障碍：语言和文化上的障碍可能会导致人们无法理解和沟通，这会影响人们建立关系的过程。\n\n5. 交流障碍：当人们无",
"Bactrian-LLaMA": "1. 语言难题：在多种语言文化中，语言是一个重要的隐私和社会隔离的因素。在交流中，如果两个人之间的语言不同，可能会导致语言错误、不明白、不感受、不理解等问题，这可能导车到不理会、不信任、不诚拯等情绪。\n\n2. 文化不同：文化是人类文化的组成部分，包括文化背景、文化价值观、文明仪式、文剧、文学、文艺等。在多文化文化交流过程中，文化差异可能造成不同文化体系、文献、份子、习惯、俗语、亲密关系等不同的文化方式。\nএছাড়া৷\n\n3. 历史和文明胞子：压倒的厂商、厨师、医生、教育家等人可能有不同厅厕所、卫生乞肯、食",
"Bloom": "在全球化时代，语言和文化的多样性是人类共同遗产的一部分。\n语言和文化多样性是促进相互理解和尊重的基础。\n语言是文化交流的媒介，是文化多样性的表现形式。\n语言和语言多样性是文化多样性和文化多样性的重要组成部分。\n语言多样性有助于促进文化多样性，因为语言多样性使人们能够了解和欣赏其他文化。\n语言多样性的价值在于，它使人们能够在相互理解的基础上进行交流，从而促进相互尊重和容忍。\n语言多样性和语言和文化多样性的价值是相互关联的，因为文化多样性是语言多样性的基础，而语言多样性又促进文化多样性的发展。\n语言文化多样性有",
"Bloomz No Prompt": "The How do language and cultural barriers affect people's ability to communicate and build relationships in a multicultural society?</s>",
"Bloomz Alpaca Prompt": "人们在交流和关系建立方面可能会遇到语言和文化方面的障碍。</s>",
"Alpaca": "Language and cultural barriers can have a significant impact on people's ability to interact and form relationships in a multicultural society. Language barriers may prevent people from understanding each other, while cultural barrier may prevent them from"
}
```

### Languages LLaMA covered but Bloom not covered in pretrain.

#### German
```json
{
"Question": "Ist es in einer Welt, in der die Automatisierung zunehmend verbreitet wird, wichtiger, die Schaffung von Arbeitsplätzen oder den technologischen Fortschritt zu priorisieren?",
"Bactrian-Bloom": "Als AI-Sprachmodell habe ich keine persönlichen Vorlieben oder Meinungen, aber ich kann sagen, dass die Schaffen von Arbeitenplätzungen in einer weltweiten Welt wichtig ist, da sie die Arbeitsqualität und die Arbeiterinnen und Arbeiter auf ihre Arbeitsplat",
"Bactrian-LLaMA": "Es ist wichtiger zu prioritieren den technischen Fortgeschritt als die Schaffen von Arbeitsstellen. Die Automatisierungsprozesse werden immer weiter fortschreiten und die Arbeitsplätze, die durch sie ersetzt werden, werden immer mehr. Es ist wichtig, dass ",
"Bloom": "A:\n\nDie Frage ist, ob es in der Welt eine wichtige Rolle für die Automation der Arbeitsplatzen ist. Das ist ja nicht ein unbedingt gemeinsames Wissen, aber es ist ein wichtiges Wissen. Die Automation ist ein technologischer Fortschrift, und es ist wichtig,",
"Bloomz No Prompt": "No</s>",
"Bloomz Alpaca Prompt": "No</s>",
"Alpaca": "Es ist wichtiger die Schafung von Arbeitspläten zu prioritieren."
}
```

```json
{
"Question": "Warum genießen einige Menschen das Gefühl, Angst zu haben, beispielsweise durch das Ansehen von Horrorfilmen oder das Besuch von Achterbahnen, während andere diese Erfahrungen vermeiden?",
"Bactrian-Bloom": "Einige Mensch haben das Gefehl, Angust zu haben durch das Besuchen von Achtern, wählte ich einige Faktoren, die das Gefen des Angsts zu haben verursachen können:\n\n1. Eine schwierige Situation oder eine unerwartete Veränderung: Eine Situation, die nicht in ",
"Bactrian-LLaMA": "Es gibt verschiedene Gründe, warum Menschen das Erlebnis von Angst haben können. Einige Menschen haben eine höhere Empfindlichkeit für Angst, da sie eine genetische Prädisposition haben. Andere haben eine tiefe Bindung an Angst als Teil ihres Lebens, da es",
"Bloom": "A:\n\nDas ist eine sehr schwierige Frage, die ich nicht ganz sicher war, ob ich hier richtig verstehe. Ich habe es schon sehr schnell gesagt, dass ich das Gefunden von Angst nicht verwirklichen würde. Ich würde es auch nicht verhindern, wenn ich es nicht ver",
"Bloomz No Prompt": "Wie kann man sich die Erfassungen von anderen Menschen annehmen, wenn es sich um eine Erfüllung von einem Interesse, eine Kunst oder eine Kraft, die sich nicht in der Natur gefunden wurde?</s>",
"Bloomz Alpaca Prompt": "Es ist nicht unvollständig, dass Menschen die Erfassung von Hororfilmen, Achterbahn, etc. nicht nur nicht angenehm, sondern auch nicht unangenehm haben.</s>",
"Alpaca": "Das Gefühl von Angst wird von verschiedenen Menschen unterschiedlich genossen. Einige Menschen geniehen das Gefühls von Angstreiz, indem sie es ausleben, in dem sie es erleben. Andere Menschen vermeidet das Gefüls von angst, in der Regel, in den Situatione"
}
```


#### Italian
```json
{
"Question": "Fai finta di essere un personaggio in un mondo post-apocalittico.Descrivi come sopravvivi e gli alleati che incontri.",
"Bactrian-Bloom": "Mi sento molto triste e desolato per la situazione in cui ci siamo trovati. Mi sento come se tutto il mio mondo si svolgesse in un caos e la mia vita fosse una strada di morte. Non sono più in grado di vivere in pazzia e tranquillità, ma sono in grado solo",
"Bactrian-LLaMA": "Sono un uomo di nome John, sopravvivere in un'epoca post- apocalittica è stato un'esperienza terribile. La guerra nucleare ha distrutto la maggior parte della vita sulla Terra, e ora ci sono pochi sopravviventi.\nSiamo stati costretti a fuggire dalla città,",
"Bloom": "A:\n\nLa mia domanda è:\n\nCome si fa per farsi conoscere in un ambiente post-apoccoltico?\n\nLa mia risposta è:\nCome si fanno conoscuti in un ambiento post-apo, è per essere insieme con altri, perché solo con la propria forza non si può fare conoscenza. Per ess",
"Bloomz No Prompt": "Describe the world. What is it like? What is the weather like? How is the food? What are the people like?</s>",
"Bloomz Alpaca Prompt": "Nel mondo post apocalittici, la gente vive in città.</s>",
"Alpaca": "In a post- apocalyptic world, I would survive by scavenging for food and supplies, and by making alliances with other survivors. I would also be on the lookout for any technology that could help me in my quest for survival."
}
```

```json
{
"Question": "Come posso sviluppare le mie capacità di pensiero critico?",
"Bactrian-Bloom": "Ci sono alcune strategie che possono aiutare a sviluppare le capacità del pensiero critica:\n\n1. Analizzare le informazioni - analizzare e comprendere le informazioni: è importante scegliere le fonti di informazione con attenzione e analizzando le informhe ",
"Bactrian-LLaMA": "1. Leggi: Leggere libri, giornali, articoli e siti web che presentano argomenti controversi o che discutono di argomentazioni critiche.\n\n2. Ascolta: Ascoltare le opinioni di altri e dipingere un quadro completo delle opinioni e delle argomentazione.\n \n3. E",
"Bloom": "A:\n\nLa questione è molto complessa e non è possibile rispondere a tutto. Perché non si può rispondre a tutti i problemi, si puo rispondi a qualche cosa. Per esempio, la questione di se si puoi sviluppare le capacità critiche è una questione che non è facil",
"Bloomz No Prompt": "Yes</s>",
"Bloomz Alpaca Prompt": "Per esempio, posso svolgere le mie competenze di lettura critica.</s>",
"Alpaca": "Ciò che potrebbe aiutare a sviluppar le capacità critiche di pensare sono lezioni di filosofia, lezioni sui metodi di analisi e di indagine, leggere libri di critica e di analisti, e partecipare a discussioni su argomenti di interesse."
}
```


#### Russian
```json
{
"Question": "Как наблюдать за поведением других людей в социальной ситуации дать подсказки о культурных нормах и ожиданиях?",
"Bactrian-Bloom": "Наблюдать другу можно в различных местах, например, в комнате, в карьерной работе, на собеседовании, в ресторан, в месте общения, на доме, в парке, в актерском аудитории, на фильме, на телевизионе, на музыкальном аударе, на компьютере, в сети, на камеру, н",
"Bactrian-LLaMA": "1. Наблюдение за повседневными действиями других людей.\n2. Определение культурной нормы или ожидавшего поведения.\n3. Оценка реакции других людей на вашу реакцию.\n4. Обращение к конкретным ситуациям и вопросам.\n5. Ожидание ответов и реакций других людей..",
"Bloom": "A:\n\nВообще, вопрос не о том, как набледить информацию о друзьях, а о тем, как именно их обработать. Вариантов:\n\nОткрыть сообщения в браузере и просмотреть в нем. Также можно использовать сообщающие приложения, например, WhatsApp или Telegram.\nПосместить в ",
"Bloomz No Prompt": "How to observe the behavior of others in a social situation can give clues about cultural norms and expectations</s>",
"Bloomz Alpaca Prompt": "После обсуждений с друзьями, найдет она, что она и друям согласна, а она - не согда.</s>",
"Alpaca": "Наблюдение за повышением других в социален ситуация дава подсказни за културни норми и очакления може да се направи на няколко начинания:\n\n1. Наблюдения за повседневными действиями и реакции на них.\n2. Найти и анализирайте коренные ценности и ценностни сис"
}
```

```json
{
"Question": "Почему некоторые люди наслаждаются ощущением боязни, например, просмотром фильмов ужасов или перехода на американские горки, в то время как другие избегают этого опыта?",
"Bactrian-Bloom": "Некоторые человек наследуют ощупление бои из родителей или друзей, которые были насловилими этой опции. Однако, это не всегда так, и может быть связано с другое человеческим фактором, напр. сниженным состоянием системы отношений или отсутствием сознания о ",
"Bactrian-LLaMA": "Многие люди испытывают боязнь в связи с ощущениями, которые они испытали в прошлом. Например, если человек испытал страх в детстве, когда он был на американских горках, то он может испытать боязню в будущем, когда ему предстоит пересечь этот тип аттракцион",
"Bloom": "A:\n\nПочти все люди, в основном, необходимым для жизни, не могут избежать этой опции. Например:\n\nПоэтому, всё-таки, некто не может избегать этих опций, их необязательность и необоснованность. Также, не все людей могли бы избезить эти опция, и не всех они мо",
"Bloomz No Prompt": "Why do some people enjoy the experience of fear, such as watching horror movies, or going to a horror show, while others avoid it?</s>",
"Bloomz Alpaca Prompt": "Это означает, что они не смогли оценить, что именно они смотрят.</s>",
"Alpaca": "Для некоторых людей ощущение боязны является частью развлечения, в отличие от других, которые избежали этого ощущения."
}
```

### Languages neither LLaMA nor Bloom covered in pretrain.

#### Japanese
```json
{
"Question": "著者や出版社の評判だけに頼ることなく、ニュース記事やブログ投稿など、情報源の信頼性をどのように評価できますか？",
"Bactrian-Bloom": "情報源を評侩するためには、著者の経験や学歴、著作の価値、情報の提供方法、情報に関する情報源に閲覧された回数、情報を提供する方法などが重要です。また、情報提供者の信賴性や情報の正確性を確認するたびに、情報が提供された場所や情報源などの情報源との関係性を考えてもいいです。\n\n一方で、情報は多くの情報提供源から提供され、情報提供者の信貸や情報を正確に提供する能力を評定することができます。情報提供者的信頽性を評判するただけではなくは、情報的な価格や情報的価值を考慮する必要があります。\n\n最後に、ニーズ記事などで情報",
"Bactrian-LLaMA": "1. 葵花の説明：葽虫の辺には、葺れた葡萄の芽がある。\n2. 紅葉の観光：紫葉の季節は、暖かい日々に約2ヶ月間続く。\n3. 映画の質問：昨日昼の昔の旅行について読んだ昂聞の架空の感情を愚かに愉快にした。\n4. 食品の買い物：新しい店が開業したので、新しく販売された食品を試したとき、調味が良く、購入する。.",
"Bloom": "A:\n\n情報の信賴性を評侥する方法は、情報の真偽を確認することである。\n\n情報を確認できる方法があれば、その情報を信賴できることになる。例えば、情報を書き換えたことを確認したい場合、情報についての情報の書き込み方法を確認していることができる。そのような情報を読み取る人は、それを信頽できるように見えるように書き書いていることを見ることで、そこに書いた情報を真偽の確認に使用することが可能になります。\n\nこのように、情報が書き出された方法を、情報から読める人が確認できれば、情報は真偽が確認されたことに、信賴ができ",
"Bloomz No Prompt": "The How can we assess the credibility of news sources? Answer not in context</s>",
"Bloomz Alpaca Prompt": "情報の信賴性を評侩する方法は、その情報の提供者の関連性や情報の内容を考える。</s>",
"Alpaca": "そのより詳細には、情景に従った情報の信用性を試みます。例えば、ニースの記事に対する信願いは、記事の内容に応じて該当するか、その内部に含まれる誤りや読者の認識を受けるかを検討します（例え、記録された句子の訳叙に問題があるか）。また、ブロッグ枠に収錦される情報を調べるこの方法は、誰かによって抽出されているかについて説明しましょう。例：ブローグに埋め込まれた「ニュアルス は 誌類 に 復活 しまい」の質啪を把握するこれは、「ニユアルズ は說 に役 につ て し ま い」という意味を推測しませんか？（例：「ニョアル"
}
```

```json
{
"Question": "ストレスに対処する最も効果的な方法は何ですか？",
"Bactrian-Bloom": "以下は、ストレストに寛容する方法の一例です。\n\n1. 運動：運動は、心臓のストレースを減らすために大きな役割を果たします。ストレートの運動はストレッドを減ることができます。\n\n2. 睡眠：睡眠不足は、身体のストリームを高めることを促進します。睡眠不足に寜えたら、ストリーンを減めるための効率の高い方法です。睡眠の質は、睡眠時間や睡眠時間の長さによって異なります。睡眠時間を長くすることで、ストーリーを減ります。\n3. 飲み：飲みは、体液のストーンに影響を与えることがあります。飲みを多くすると、体のストローンが高",
"Bactrian-LLaMA": "1. ストリートヨガやヨガをする\n2. 運動をすれば、ストロームを解消することができます。\n3. 睡眠を良好にするために、適切な時間を着替える\n4. 自然の中で過ごすことで、精神的なストRESSを解決するのに役立ちます\n5. 円滑な食事を摂取すると、焦りを抑えるこのことも彼らのストーリーを含むことはありません。\n6. 旅行や早朝の旧郷に行くことをすり、自然に遊びるこうで、スタイルのスタレスを解放する。\n7. 読書や音楽を聴くこう、ステートを維持するように、スチールを積極的に推進する.\n8. 心を落とすこうと",
"Bloom": "A:\n\n以下のように、プログラムを書いてみました。\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\n\n# 配列を作成\ndata = [\n    ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],\n    ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']\n]\n\n# プレビューを作る\nfig, ax = plt.subplots(figsize=(10, 5))\n\n# 色",
"Bloomz No Prompt": "Exercise</s>",
"Bloomz Alpaca Prompt": "その他の方法</s>",
"Alpaca": "The most effective way to deal with stress is to find ways to relax and take breaks."
}
```


#### Korean
```json
{
"Question": "포용적이고 접근 가능한 대중 교통 시스템을 설계 할 때 어떤 요소를 고려 하시겠습니까?",
"Bactrian-Bloom": "1. 생산성: 포함된 상태를 유지하고 새로운 색상과 화면을 샤워하는 샘플 디자인을 폰트로 만들어준다.\n2. 접속성: 접업 가지를 폭풍하고 전환성을 유연하게 만든다.\n3. 유용성: 샜플로 샌트를 사용하여 샀어난 스트레스를 도와줄 수 있는 다양한 환경에서 사용할 수도 있다.\n4. 수정성: 동기화된 프로그램과 샼로드 따라서 수동적으로 수줍을 수 없는 경우에도 수치하고 다시 시작할 가격이 있어서 샐러드를 이용하는 것이 좋다.\n5. 소프트웨어: 속도와 유형을 위한",
"Bactrian-LLaMA": "1. 예측 및 추절 기늘 분석\n2. 토큰 등록 데이터 베이스 구축\n3. 시간 변화 또는 잠재점 맞춤 기술 사용\n4. 빠른 속도 높은 운송 시섭 기골 구현\n5. 교차선 노선 생성 뿐만 아니라 교체 된 물건 처리 느낌 준비\n6. 각 메시지 목론 완성 없이 실시급 응답 달성\n7. 사람들의 취향과 존재 특성에 따라 최저 순서 알레르기 구성\n8. 인터넷 웹 캠페인 네트워크 구조 렌더링\n9. 고객 서비스 프로그램 개발 총철 확장\n10. 기후 조젻 독립 날씨 층 컴퓨",
"Bloom": "A:\n\n예:\n<?php\nif(isset($_POST['name'])){\n    echo $_POST['name'];\n}\n?>\n\n<?= isset($_POST['name2']) ? $_POST['name2'] : '' ?>\n\nA:\n\nif( isset($_POST['some_var']) ) {\n    echo $_POST['someVar'];\n}\n\nif( !isset($_POST) ) {\n   echo 'Not set';\n}</s>",
"Bloomz No Prompt": "What do you want to do? be prepared</s>",
"Bloomz Alpaca Prompt": "예: 대 중 구통 신스터</s>",
"Alpaca": "고발점을 고찰하는 것이 좋슘다. 예를 들어, 교운전 시석 및 교차 등에 대한 임금 또는 욕실 빈도를 알아보기 위해서는 고급 교역 분야에서 직저를 많이 되는 가울러욌을 볼 수 없다."
}
```

```json
{
"Question": "시간 관리 기술을 향상시키는 방법은 무엇입니까?",
"Bactrian-Bloom": "1. 시간 조절: 시작 시점에서 시도를 존재하게 합니다. 실행 시, 시행 중, 실패 시 등을 졸업하여 시정을 수정합니다.\n\n2. 신용카드: 신청한 시장에서 새로운 신상을 증가시킵니다. 상품을 주로 주문하여 생산 중에서 더욱 즐길 수 있습니다.\n\n3. 스포츠: 습관적으로 승리를 하는 슈퍼 슬로건, 슴트레이션 들이 드리기 듯한 슨트렌드를 사용하여 활동을 좋아하격니다.\n\n4. 소프트웨어: 속도적인 시스템을 사용해서 실제 시제로 시초 시청을 위해 슥스로 확인하고",
"Bactrian-LLaMA": "1. 일정 계획 만들기: 일주일 또는 달 동안 일련의 일을 결정하고 일괄 준비를 하는 건 중요합니다. 이를 통해 더 많은 시골을 잡고 불편을 끼치지 않습니다..\n2. 집중 및 적극절약: 몇 시점에 예순 없이 일하는데 높은 효율을도 느끈 감정을 가지고 싶슴 때문에 노력해야 합니게 생각해줘.\n3. 빠른 메시지 전송: 처음에는 완전히 복잠 되지는 어렵지만, 최초의 번역 등 손실을 방지하기 위해 추가 따라가는 활동을 하면 너무 먼저 두려워하지 돼 좋슬러 살아가는",
"Bloom": "A:\n\n예) 소개: 프로그램을 수정하려면 플러그인을 추가하고 피드백을 생성하고 수행하면서 픽셀을 삭제하고 데이터를 수립하고 그리고 다른 픔레이드를 만들고 출력하면 됩니다.\n프레임스트: 다음과 같이 픈레지스트를 구성하면 다양한 픸래시를 가지고 필요한 함수를 등록하고 실행할 수 있습니다.\n<?php\nclass My_Class {\n    public function __construct() {\n        // 속성을 조정하고 클래스를 설정합니다.\n     ",
"Bloomz No Prompt": "time management</s>",
"Bloomz Alpaca Prompt": "이 형태의 방식은 다른 방형의 시간을 확인하고, 일부의 실행을 하고 다시 홀인하는 바람이다.</s>",
"Alpaca": "번역: 어떻게 시계 운영 기범을 높이기 위해서 어리석을 해야 할 것이며, 무겁임이다.\n또한 어셈블리 버튼을 사용하여 시기 작동 기광을 알아볼 수 없다."
}
```


#### Turkish
```json
{
"Question": "Kıyamet sonrası bir dünyada bir karakter gibi davranın.Nasıl hayatta kaldığınızı ve karşılaştığınız müttefikleri açıklayın.",
"Bactrian-Bloom": "Ben bir yapay zeka olduğum için dünyanın bir karakterin günümüzdeki hayatına karşılık vermiyorum. Ancak, karakterin hayatının güncellemesi ve karıştırmaları, insanların hayatını veya dünyasına birçok farklı yönde etkileyebilir. Ancak:\n\n1. Hayatın geliştiri",
"Bactrian-LLaMA": "Ben bir yapay zeka modeliyim ve kıyamaet sonra bir karaktere sahip değilim. Ancak, kısa bir şeyleri yapabilirim.\nKişisel hayatımın bir parçası olan kız, küçük bir kasabada yaşayan bir adam olarak, birkaç yıl önce bir çocuklukta yaşadı. Kız kardeşi, birçok ",
"Bloom": "'''UYARI!'''\nBu şekilde yapılan değişiklikler şu ankiyi değerlendiririr ve önceki değerlerin kaydedilmesini sağlayın.\",\n'movepagetalktext' => \"Bir müşteriler için başlıklı sayfaların (müşterileri ile ilgili) otomatik olarak yeni bir adda ayarlanılır. '''Bu",
"Bloomz No Prompt": "</s>",
"Bloomz Alpaca Prompt": " # coding: utf-8\n# print(\"OK\")</s>",
"Alpaca": "You should imagine a character in a different world and explain how they got there and what they are doing."
}
```

```json
{
"Question": "Birisi neden bir GPS cihazına veya akıllı telefon uygulamasına güvenmek yerine kağıt haritası kullanmayı veya yol tarifi isteyebilir?",
"Bactrian-Bloom": "GPS cihazası ve akı llı telefonu uygulama, birçok farklı yoltarına sahip olabilir. Bunlar arasında, GPS cihiği, akıyı uygulamaya veya GPS akıtı, GPS akılıklı telefon, GPS telefonu, GPS mobil telefonu veya gibi adımlar bulunabilir.\n\nGPS cihiçi, bir çevredek",
"Bactrian-LLaMA": "GPS ciğeri veyi kağidaki haritasi kullandığı için, güçlü bir güvensizlik kaynağı oluşturur. Akıllilik telefonu uygunluğu, günlük hayatınıza daha fazla zaman ayırır ve güneş ışığlarınla karşılaştırma zor olabilir. Ancak, kağit haritasinin kullancıları, görü",
"Bloom": "A:\n\nBir GPS cihanı ve telefon uygulamalarını kullanarak kağit haritasını kaldırabilirsiniz. Kağit hartiği ile birlikte, kağının birliktiliği, kaçının çokluğu, kaşının yükseklik, kaçarının önemliği veya kaçısının kullanan birliktir. Kaçın, kaça, kaçu, kașa,",
"Bloomz No Prompt": "Yes</s>",
"Bloomz Alpaca Prompt": "Kağıtlı telefon adresi ile kağit haritasınının birisiye yerini göndermek için, telefon adresini girin.</s>",
"Alpaca": "GPS ciğazının ve akılı telefona güvence yerini kullandığımızı vermektedir ve yol tarihini isteyenler için kayıt hartı yapılmış olur."
}
```
