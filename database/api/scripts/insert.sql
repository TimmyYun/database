USE dev;

INSERT INTO diseasetype VALUES (0, "acquired disease is one that began at some point during one's lifetime");
INSERT INTO diseasetype VALUES (1, "acute disease is one of a short-term nature (acute)");
INSERT INTO diseasetype VALUES (2, "chronic disease is one that persists over time");
INSERT INTO diseasetype VALUES (3, "congenital disorder is one that is present at birth");
INSERT INTO diseasetype VALUES (4, "virology");
INSERT INTO diseasetype VALUES (5, "hereditary disease is a type of genetic disease caused by genetic mutations that are hereditary");
INSERT INTO diseasetype VALUES (6, "iatrogenic disease or condition is one that is caused by medical intervention");
INSERT INTO diseasetype VALUES (7, "idiopathic disease has an unknown cause or source");
INSERT INTO diseasetype VALUES (8, "disease that cannot be cured");
INSERT INTO diseasetype VALUES (9, "infectious diseases");

INSERT INTO country VALUES("USA", 332403650);
INSERT INTO country VALUES("Kazakhstan", 19308484);
INSERT INTO country VALUES("Russia", 146082519);
INSERT INTO country VALUES("China", 1425887337);
INSERT INTO country VALUES("India", 1407563842);
INSERT INTO country VALUES("Japan", 128547854);
INSERT INTO country VALUES("Korea", 51844834);
INSERT INTO country VALUES("United Kingdom", 67081234);
INSERT INTO country VALUES("Turkey", 84680273);
INSERT INTO country VALUES("Italy", 60461826);

INSERT INTO disease VALUES("Adenoviruses","Virus","Adenoviruses are medium-sized, nonenveloped viruses with an icosahedral nucleocapsid containing a double-stranded DNA genome", 0);
INSERT INTO disease VALUES("Coxsackievirus","Virus","Coxsackieviruses are belong to the Picornaviridae family of nonenveloped, linear, positive-sense single-stranded RNA viruses", 1);
INSERT INTO disease VALUES("covid-19","bacteria","Salmonella is a genus of rod-shaped Gram-negative bacteria of the family Enterobacteriaceae", 2);
INSERT INTO disease VALUES("Bacillus","bacteria","Bacillus is a genus of Gram-positive, rod-shaped bacteria, a member of the phylum Bacillota", 3);
INSERT INTO disease VALUES("Yeasts","Fungi","Yeasts are eukaryotic, single-celled microorganisms classified as members of the fungus kingdom", 4);
INSERT INTO disease VALUES("Molds","Fungi","A mold or mould is one of the structures certain fungi can form", 5);
INSERT INTO disease VALUES("Fungi","Parasites","A fungus is any member of the group of eukaryotic organisms", 6);
INSERT INTO disease VALUES("Leeches","Parasites","Leeches are segmented parasitic or predatory worms that comprise the subclass Hirudinea within the phylum Annelida", 7);
INSERT INTO disease VALUES("Lice","Parasites","Louse is the common name for any member of the clade Phthiraptera", 8);
INSERT INTO disease VALUES("Viruses","Parasites","A virus is a submicroscopic infectious agent that replicates only inside the living cells of an organism", 9);

INSERT INTO discover VALUES("USA", "1910-01-01", "Adenoviruses");
INSERT INTO discover VALUES("Kazakhstan", "1920-01-01", "Coxsackievirus");
INSERT INTO discover VALUES("Russia", "1930-01-01", "covid-19");
INSERT INTO discover VALUES("China", "1940-01-01", "Bacillus");
INSERT INTO discover VALUES("India", "1950-01-01", "Yeasts");
INSERT INTO discover VALUES("Japan", "1960-01-01", "Molds");
INSERT INTO discover VALUES("Korea", "1970-01-01", "Fungi");
INSERT INTO discover VALUES("United Kingdom", "1980-01-01", "Leeches");
INSERT INTO discover VALUES("Turkey", "1990-01-01", "Lice");
INSERT INTO discover VALUES("Italy", "2000-01-01", "Viruses");

INSERT INTO users VALUES("a@gmail.com", "Erasyl", "Imaginary1", 100000, "+77000000001", "USA");
INSERT INTO users VALUES("b@gmail.com", "Timur", "Imaginary2", 200000, "+77000000002", "Kazakhstan");
INSERT INTO users VALUES("c@gmail.com", "Ali", "Imaginary3", 300000, "+77000000003", "Russia");
INSERT INTO users VALUES("d@gmail.com", "Ramazan", "Imaginary4", 400000, "+77000000004", "China");
INSERT INTO users VALUES("e@gmail.com", "Samir", "Imaginary5", 500000, "+77000000005", "India");
INSERT INTO users VALUES("f@gmail.com", "Anel", "Imaginary6", 600000, "+77000000006", "Japan");
INSERT INTO users VALUES("g@gmail.com", "Sat", "Imaginary7", 700000, "+77000000007", "Korea");
INSERT INTO users VALUES("h@gmail.com", "Bexultan", "Imaginary8", 800000, "+77000000008", "United Kingdom");
INSERT INTO users VALUES("i@gmail.com", "Karina", "Imaginary9", 900000, "+77000000009", "Turkey");
INSERT INTO users VALUES("j@gmail.com", "Ester", "Imaginary10", 1000000, "+77000000010", "Italy");
INSERT INTO users VALUES("k@gmail.com", "Erasyl2", "Imaginary11", 1100000, "+77000000011", "USA");
INSERT INTO users VALUES("l@gmail.com", "Timur2", "Imaginary12", 1200000, "+77000000012", "Kazakhstan");
INSERT INTO users VALUES("m@gmail.com", "BekTest", "Imaginary13", 1300000, "+77000000013", "Kazakhstan");
INSERT INTO users VALUES("n@gmail.com", "Beksssss", "Imaginary14", 1400000, "+77000000014", "China");
INSERT INTO users VALUES("o@gmail.com", "gulAAA", "Imaginary15", 1500000, "+77000000015", "India");
INSERT INTO users VALUES("p@gmail.com", "AAAGul", "Imaginary16", 1600000, "+77000000016", "Japan");
INSERT INTO users VALUES("q@gmail.com", "Sat2", "Imaginary17", 1700000, "+77000000017", "Korea");
INSERT INTO users VALUES("r@gmail.com", "Bexultan2", "Imaginary18", 1800000, "+77000000018", "United Kingdom");
INSERT INTO users VALUES("s@gmail.com", "Karina2", "Imaginary19", 1900000, "+77000000019", "Turkey");
INSERT INTO users VALUES("t@gmail.com", "Ester2", "Imaginary20", 2000000, "+77000000020", "Italy");

INSERT INTO publicservant VALUES("a@gmail.com", "Department 1");
INSERT INTO publicservant VALUES("b@gmail.com", "Department 2");
INSERT INTO publicservant VALUES("c@gmail.com", "Department 1");
INSERT INTO publicservant VALUES("d@gmail.com", "Department 4");
INSERT INTO publicservant VALUES("e@gmail.com", "Department 5");
INSERT INTO publicservant VALUES("f@gmail.com", "Department 6");
INSERT INTO publicservant VALUES("g@gmail.com", "Department 7");
INSERT INTO publicservant VALUES("h@gmail.com", "Department 8");
INSERT INTO publicservant VALUES("i@gmail.com", "Department 9");
INSERT INTO publicservant VALUES("j@gmail.com", "Department 10");

INSERT INTO doctor VALUES("k@gmail.com", "Degree 1");
INSERT INTO doctor VALUES("l@gmail.com", "Degree 2");
INSERT INTO doctor VALUES("m@gmail.com", "Degree 3");
INSERT INTO doctor VALUES("n@gmail.com", "Degree 4");
INSERT INTO doctor VALUES("o@gmail.com", "Degree 5");
INSERT INTO doctor VALUES("p@gmail.com", "Degree 6");
INSERT INTO doctor VALUES("q@gmail.com", "Degree 7");
INSERT INTO doctor VALUES("r@gmail.com", "Degree 8");
INSERT INTO doctor VALUES("s@gmail.com", "Degree 9");
INSERT INTO doctor VALUES("t@gmail.com", "Degree 10");

INSERT INTO specialize VALUES(0 ,0 ,"k@gmail.com");
INSERT INTO specialize VALUES(1 ,1 ,"k@gmail.com");
INSERT INTO specialize VALUES(2 ,2 ,"k@gmail.com");
INSERT INTO specialize VALUES(3 ,1 ,"l@gmail.com");
INSERT INTO specialize VALUES(4 ,4 ,"l@gmail.com");
INSERT INTO specialize VALUES(5 ,6 ,"l@gmail.com");
INSERT INTO specialize VALUES(6 ,2 ,"m@gmail.com");
INSERT INTO specialize VALUES(7 ,4 ,"m@gmail.com");
INSERT INTO specialize VALUES(8 ,3 ,"n@gmail.com");
INSERT INTO specialize VALUES(9 ,4 ,"o@gmail.com");
INSERT INTO specialize VALUES(10 ,5 ,"p@gmail.com");
INSERT INTO specialize VALUES(11 ,6 ,"q@gmail.com");
INSERT INTO specialize VALUES(12 ,7 ,"r@gmail.com");
INSERT INTO specialize VALUES(13 ,8 ,"s@gmail.com");
INSERT INTO specialize VALUES(14 ,9 ,"s@gmail.com");
INSERT INTO specialize VALUES(15 ,8 ,"t@gmail.com");
INSERT INTO specialize VALUES(16 ,9 ,"t@gmail.com");

INSERT INTO record VALUES("a@gmail.com", "USA", "covid-19", 100000, 200000);
INSERT INTO record VALUES("a@gmail.com", "Kazakhstan", "covid-19", 100000, 200000);
INSERT INTO record VALUES("a@gmail.com", "Russia", "covid-19", 100000, 200000);
INSERT INTO record VALUES("a@gmail.com", "India", "covid-19", 100000, 200000);
INSERT INTO record VALUES("a@gmail.com", "China", "covid-19", 100000, 200000);
INSERT INTO record VALUES("b@gmail.com", "Japan", "covid-19", 200000, 300000);
INSERT INTO record VALUES("b@gmail.com", "Turkey", "covid-19", 200000, 300000);
INSERT INTO record VALUES("b@gmail.com", "Kazakhstan", "Coxsackievirus", 200000, 300000);
INSERT INTO record VALUES("c@gmail.com", "Russia", "covid-19", 300000, 400000);
INSERT INTO record VALUES("c@gmail.com", "USA", "covid-19", 300000, 400000);
INSERT INTO record VALUES("c@gmail.com", "Kazakhstan", "covid-19", 300000, 400000);
INSERT INTO record VALUES("d@gmail.com", "China", "Bacillus", 400000, 500000);
INSERT INTO record VALUES("e@gmail.com", "India", "Yeasts", 500000, 600000);
INSERT INTO record VALUES("f@gmail.com", "Japan", "Molds", 600000, 700000);
INSERT INTO record VALUES("g@gmail.com", "Korea", "Fungi", 700000, 800000);
INSERT INTO record VALUES("h@gmail.com", "United Kingdom", "Leeches", 800000, 900000);
INSERT INTO record VALUES("i@gmail.com", "Turkey", "Lice", 900000, 1000000);
INSERT INTO record VALUES("j@gmail.com", "Italy", "Viruses", 1000000, 1100000);

