--liquibase formatted sql

--changeset shal1928:initial-KAS
--comment CREATE TABLE KAS: Knowledge Accumulation Stage
CREATE TABLE KAS(
    TITLE TEXT NOT NULL
);