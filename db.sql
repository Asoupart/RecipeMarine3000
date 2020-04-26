BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "recipes" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"nbr_person"	INTEGER,
	"id_src"	INTEGER,
	FOREIGN KEY("id_src") REFERENCES "sources"("id")
);
CREATE TABLE IF NOT EXISTS "sources" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "sections" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	VARCHAR(255),
	"id_recipe"	INTEGER,
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id")
);
CREATE TABLE IF NOT EXISTS "images" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"id_recipe"	INTEGER,
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id")
);
CREATE TABLE IF NOT EXISTS "map_recipe_category" (
	"id_recipe"	INTEGER,
	"id_category"	INTEGER,
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id"),
	FOREIGN KEY("id_category") REFERENCES "categories"("id")
);
CREATE TABLE IF NOT EXISTS "map_recipe_tool" (
	"id_recipe"	INTEGER,
	"id_tool"	INTEGER,
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id"),
	FOREIGN KEY("id_tool") REFERENCES "tools"("id")
);
CREATE TABLE IF NOT EXISTS "tools" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "categories" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "map_section_ingredient" (
	"id_section"	INTEGER NOT NULL,
	"id_ingredient"	INTEGER NOT NULL,
	"quantity"	INTEGER NOT NULL,
	"unit"	TEXT,
	CONSTRAINT "map_section_ingredient_FK" FOREIGN KEY("id_ingredient") REFERENCES "ingredients"("id"),
	CONSTRAINT "map_section_ingredient_FK_1" FOREIGN KEY("id_section") REFERENCES "sections"("id")
);
CREATE TABLE IF NOT EXISTS "instructions" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"text_ins"	VARCHAR(255),
	"id_section"	INTEGER NOT NULL,
	CONSTRAINT "map_section_FK" FOREIGN KEY("id_section") REFERENCES "sections"("id")
);
CREATE TABLE IF NOT EXISTS "ingredients" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	VARCHAR(255)
);
INSERT INTO "sources" VALUES (1,'Marine');
INSERT INTO "sources" VALUES (2,'moi');
INSERT INTO "tools" VALUES (1,'Four');
INSERT INTO "tools" VALUES (2,'Batteur');
INSERT INTO "tools" VALUES (3,'Cellule');
INSERT INTO "categories" VALUES (2,'survie');
INSERT INTO "ingredients" VALUES (1,'farine');
INSERT INTO "ingredients" VALUES (2,'sel');
INSERT INTO "ingredients" VALUES (4,'patate');
INSERT INTO "ingredients" VALUES (5,'sucre');
INSERT INTO "ingredients" VALUES (6,'concombre');
INSERT INTO "ingredients" VALUES (7,'oeuf');
INSERT INTO "ingredients" VALUES (8,'lait');
INSERT INTO "ingredients" VALUES (9,'carotte');
INSERT INTO "ingredients" VALUES (12,'beurre');
INSERT INTO "ingredients" VALUES (13,'pâtes');
COMMIT;
