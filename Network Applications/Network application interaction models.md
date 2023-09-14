# Protocols
ISO/OSI
Прикладной
HTTP, SMTP, POP3, TELNET
Представительский
ASCII, EBCDIC, SSL, gzip
Сессионный

# ISO/OSI

OSI stands for **Open Systems Interconnection**. It has been developed by ISO – ‘**International Organization for Standardization**‘, in the year 1984. It is a 7-layer architecture with each layer having specific functionality to perform. All these 7 layers work collaboratively to transmit the data from one person to another across the globe.

![[ISO_OSI+TCP_IP.png]]

Consists of 7 primary levels:

## **Physical level.**

The physical layer defines the properties of the data transmission medium (coaxial cable, twisted pair, fiber optic channel, etc.) and methods of its connection
cable adapters: cable specifications (resistance, capacitance,
isolation, etc.), a list of valid connectors, signal processing methods, etc.

<span style='color: #FFFF00;'>  RU </span>
Начнем с самого нижнего уровня. Он отвечает за обмен физическими сигналами между физическими устройствами, «железом». Компьютерное железо не понимает, что такое картинка или что на ней изображено, «железу» картинка понятна только в виде набора нулей и единиц, то есть бит.
Устройства физического уровня оперируют битами. Они передаются по кабелям (например, через оптоволокно) или без — например, через Bluetooth или IRDA, Wi-Fi, GSM, 4G и так далее.

**---**

## **Link layer.**

At the link level of the model, two sublevels are considered:
a sublevel of access control to the data transmission medium and a sublevel of control of the logical channel. Access control to the data transmission medium defines the methods of the use of network adapters of the data transmission medium. Control sublayer
logical link defines the concept of a channel between two network adapters, as well as
methods for detecting and correcting data transmission errors. The main purpose of the process fools the link layer to prepare a block of data (commonly called a frame) for the next
general network layer.
There are two points to note here:
1) starting from the logical link control sublayer and above, the protocols do not
depend on the data transmission medium;
2) to organize a local network, only physical and channel levels, but such a network will not be scalable (cannot expand), because has a limited specific addressing capabilities and does not have routing functions.

<span style='color: #FFFF00;'>  RU </span>
Когда два пользователя находятся в одной сети, состоящей только из двух устройств, — это идеальный случай. Но что если этих устройств больше?

Второй уровень решает проблему адресации при передаче информации. Канальный уровень получает биты и превращает их в кадры (frame, также «фреймы»). Задача здесь — сформировать кадры с адресом отправителя и получателя, после чего отправить их по сети.

У канального уровня есть два подуровня — это MAC и LLC. MAC (Media Access Control, контроль доступа к среде) отвечает за присвоение физических MAC-адресов, а LLC (Logical Link Control, контроль логической связи) занимается проверкой и исправлением данных, управляет их передачей. Для упрощения мы указываем LLC на втором уровне модели, но, если быть точными, LLC нельзя отнести полностью ни к первому, ни ко второму уровню — он между.

На втором уровне OSI работают коммутаторы, их задача — передать сформированные кадры от одного устройства к другому, используя в качестве адресов только физические MAC-адреса.

На канальном уровне активно используется протокол ARP (Address Resolution Protocol — протокол определения адреса). С помощью него 64-битные MAC-адреса сопоставляются с 32-битными IP-адресами и наоборот, тем самым обеспечивается инкапсуляция и декапсуляция данных.
**---**

## **Network layer.**

The network layer defines addressing and routing methods for the computers on the network. Unlike the link layer, the network layer defines a single addressing method for all computers on the network regardless of the method of data transmission. This level defines how computer networks are connected. The result of the procedures of the network layer is the packet that is processed by the transport layer procedures.

<span style='color: #FFFF00;'>  RU </span>
На третьем уровне появляется новое понятие — маршрутизация. Для этой задачи были созданы устройства третьего уровня — маршрутизаторы (их еще называют роутерами). Маршрутизаторы получают MAC-адрес от коммутаторов с предыдущего уровня и занимаются построением маршрута от одного устройства к другому с учетом всех потенциальных неполадок в сети.
Над канальным уровнем находится следующий – сетевой. На этой ступени вводятся понятия «маршрутизация» и «IP-адрес». Для трансформации MAC-адресов в IP применяется протокол ARP.

Здесь осуществляется маршрутизация трафика. Когда пользователь, к примеру, желает перейти на сайт и вводит его адрес, отправляется DNS-запрос. Ответом на него будет IP-адрес, который подставляется в пакет. Пакет данных – это новый термин, который появляется на 3-м сетевом уровне.

Устройствами здесь являются роутер или маршрутизатор.
**---**

## **Transport layer.**

The main purpose of the transport layer procedures is
preparation and delivery of data packets between endpoints without errors and in the right
random sequence. The transport layer procedures generate files for the session
layer from packets received from the network layer.

<span style='color: #FFFF00;'> RU </span>
Все семь уровней модели OSI можно условно разделить на две группы:

- Media layers (уровни среды),
- Host layers (уровни хоста).

Уровни группы Media Layers (L1, L2, L3) занимаются передачей информации (по кабелю или беспроводной сети), используются сетевыми устройствами, такими как коммутаторы, маршрутизаторы и т.п. Уровни группы Host Layers (L4, L5, L6, L7) используются непосредственно на устройствах, будь то стационарные компьютеры или мобильные устройства.

Четвертый уровень — это посредник между Host Layers и Media Layers, относящийся скорее к первым, чем к последним. Его главной задачей является транспортировка пакетов. Естественно, при транспортировке возможны потери, но некоторые типы данных более чувствительны к потерям, чем другие. Например, если в тексте потеряются гласные, то будет сложно понять смысл, а если из видеопотока пропадет пара кадров, то это практически никак не скажется на конечном пользователе. Поэтому при передаче данных, наиболее чувствительных к потерям на транспортном уровне, используется протокол TCP, контролирующий целостность доставленной информации.

Для мультимедийных файлов небольшие потери не так важны, гораздо критичнее будет задержка. Для передачи таких данных, наиболее чувствительных к задержкам, используется протокол UDP, позволяющий организовать связь без установки соединения.

При передаче по протоколу TCP данные делятся на сегменты. Сегмент — это часть пакета. Когда приходит пакет данных, который превышает пропускную способность сети, пакет делится на сегменты допустимого размера. Сегментация пакетов также требуется в ненадежных сетях, когда существует большая вероятность того, что большой пакет будет потерян. При передаче данных по протоколу UDP пакеты данных делятся уже на датаграммы. Датаграмма (datagram) — это тоже часть пакета, но ее нельзя путать с сегментом.

Главное отличие датаграмм — в автономности. Каждая датаграмма содержит все необходимые заголовки, чтобы дойти до конечного адресата, поэтому они не зависят от сети, могут доставляться разными маршрутами и в разном порядке. При потере датаграмм или сегментов получаются «битые» куски данных, которые не получится корректно обработать.

Первые четыре уровня — специализация сетевых инженеров. С последними тремя они не так часто сталкиваются, потому что пятым, шестым и седьмым занимаются разработчики.
**---**

## **Session level.** 

The session layer will determine how to set up and tear down
connections (called sessions) between two applications running on a network.
It should be noted that the session layer is the point of interaction between programs and computer network.

<span style='color: #FFFF00;'>  RU </span>
Пятый уровень оперирует чистыми данными. Помимо пятого, чистые данные используются также на шестом и седьмом уровне. Сеансовый уровень отвечает за поддержку сеанса или сессии связи. Пятый уровень оказывает услугу следующему: управляет взаимодействием между приложениями, открывает возможности синхронизации задач, завершения сеанса, обмена информации.

Службы сеансового уровня зачастую применяются в средах приложений, требующих удаленного вызова процедур, т.е. чтобы запрашивать выполнение действий на удаленных компьютерах или независимых системах на одном устройстве (при наличии нескольких ОС).

Примером работы пятого уровня может служить видеозвонок по сети. Во время видеосвязи необходимо, чтобы два потока данных (аудио и видео) шли синхронно. Когда к разговору двоих человек прибавится третий — получится уже конференция. Задача пятого уровня — сделать так, чтобы собеседники могли понять, кто сейчас говорит.
**---**

## **Presentation level.** 

At the representative level, the data format is defined by applications. The procedures at this level describe how to encrypt, compress and transform of data character sets.

<span style='color: #FFFF00;'>  RU </span>

**Представительский уровень**

О задачах уровня представления вновь говорит его название. Шестой уровень отвечает за преобразование протоколов и кодирование/декодирование данных. Шестой уровень также занимается представлением картинок (в JPEG, GIF и т.д.), а также видео-аудио (в MPEG, QuickTime). А помимо этого → шифрованием данных, когда при передаче их необходимо защитить.

**---**

## **Application level.**

The main purpose of the level: to determine the ways of interaction
actions of users with the system (define the interface).

Protocols: HTTP, SMTP, POP3, TelNet, etc.

<span style='color: #FFFF00;'>  RU </span>
Седьмой уровень иногда еще называют уровень приложений, но чтобы не запутаться можно использовать оригинальное название — application layer. Прикладной уровень — это то, с чем взаимодействуют пользователи, своего рода графический интерфейс всей модели OSI, с другими он взаимодействует по минимуму.

Все услуги, получаемые седьмым уровнем от других, используются для доставки данных до пользователя. Протоколам седьмого уровня не требуется обеспечивать маршрутизацию или гарантировать доставку данных, когда об этом уже позаботились предыдущие шесть. Задача седьмого уровня — использовать свои протоколы, чтобы пользователь увидел данные в понятном ему виде.


# TCP/IP

![[OSI->TCP_IP.png]]


## Difference between TCP/IP and OSI Model

1. TCP refers to Transmission Control Protocol. OSI refers to Open Systems Interconnection.
2. TCP/IP uses both the session and presentation layer in the application layer itself.OSI uses different session and presentation layers.
3. TCP/IP follows connectionless a horizontal approach. OSI follows a vertical approach.
4. The Transport layer in TCP/IP does not provide assurance delivery of packets. In the OSI model, the transport layer provides assurance delivery of packets.
5. Protocols cannot be replaced easily in TCP/IP model. While in the OSI model, Protocols are better covered and are easy to replace with the technology change.
6. TCP/IP model network layer only provides connectionless services. Connectionless and connection-oriented services are provided by the network layer in the OSI model.