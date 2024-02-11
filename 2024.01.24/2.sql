drop database if exist mus_library;
create database mus_library;
use mus_library;

create table singers (
    id smallint unsigned PRIMARY KEY auto_increment,
    singer_name varchar(50) not null
    );

create table styles (
    id smallint unsigned PRIMARY KEY auto_increment,
    style_name varchar(50) not null
    );

create table publishers (
    id smallint unsigned PRIMARY KEY auto_increment,
    publisher_name varchar(50) not null,
    publisher_country varchar(50) not null
    );

create table collections (
    id smallint unsigned PRIMARY KEY auto_increment,
    collection_name varchar(50) not null,
    singer_name varchar(50) not null
        REFERENCES singers(singer_name),
    relese_date date not null,
    style_name varchar(50) not null
        REFERENCES styles(style_name),
    publisher_name varchar(50) not null
        REFERENCES publishers(publisher_name)
    )

create table songs (
    id smallint unsigned PRIMARY KEY auto_increment,
    song_name varchar(50) not null,
    singer_name varchar(50) not null 
        REFERENCES singers(singer_name),
    collection_name varchar(50) not null 
        REFERENCES collections(collection_name),
    style_name varchar(50) not null
        REFERENCES styles(style_name),
    publisher_name varchar(50) not null
        REFERENCES publishers(publisher_name)
);