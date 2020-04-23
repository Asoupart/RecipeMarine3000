BEGIN TRANSACTION;
DROP TABLE IF EXISTS "ingredients";
CREATE TABLE IF NOT EXISTS "ingredients" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	VARCHAR(255)
);
DROP TABLE IF EXISTS "instructions";
CREATE TABLE IF NOT EXISTS "instructions" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"text_ins"	VARCHAR(255),
	"id_section"	INTEGER NOT NULL,
	CONSTRAINT "map_section_FK" FOREIGN KEY("id_section") REFERENCES "sections"("id")
);
DROP TABLE IF EXISTS "map_section_ingredient";
CREATE TABLE IF NOT EXISTS "map_section_ingredient" (
	"id_section"	INTEGER NOT NULL,
	"id_ingredient"	INTEGER NOT NULL,
	"quantity"	INTEGER NOT NULL,
	"unit"	TEXT,
	CONSTRAINT "map_section_ingredient_FK" FOREIGN KEY("id_ingredient") REFERENCES "ingredients"("id"),
	CONSTRAINT "map_section_ingredient_FK_1" FOREIGN KEY("id_section") REFERENCES "sections"("id")
);
DROP TABLE IF EXISTS "categories";
CREATE TABLE IF NOT EXISTS "categories" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL
);
DROP TABLE IF EXISTS "tools";
CREATE TABLE IF NOT EXISTS "tools" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL
);
DROP TABLE IF EXISTS "map_recipe_tool";
CREATE TABLE IF NOT EXISTS "map_recipe_tool" (
	"id_recipe"	INTEGER,
	"id_tool"	INTEGER,
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id"),
	FOREIGN KEY("id_tool") REFERENCES "tools"("id")
);
DROP TABLE IF EXISTS "map_recipe_category";
CREATE TABLE IF NOT EXISTS "map_recipe_category" (
	"id_recipe"	INTEGER,
	"id_category"	INTEGER,
	FOREIGN KEY("id_category") REFERENCES "categories"("id"),
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id")
);
DROP TABLE IF EXISTS "images";
CREATE TABLE IF NOT EXISTS "images" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"id_recipe"	INTEGER,
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id")
);
DROP TABLE IF EXISTS "sections";
CREATE TABLE IF NOT EXISTS "sections" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	VARCHAR(255),
	"id_recipe"	INTEGER,
	FOREIGN KEY("id_recipe") REFERENCES "recipes"("id")
);
DROP TABLE IF EXISTS "sources";
CREATE TABLE IF NOT EXISTS "sources" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL
);
DROP TABLE IF EXISTS "recipes";
CREATE TABLE IF NOT EXISTS "recipes" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"nbr_person"	INTEGER,
	"id_src"	INTEGER,
	FOREIGN KEY("id_src") REFERENCES "sources"("id")
);
COMMIT;
