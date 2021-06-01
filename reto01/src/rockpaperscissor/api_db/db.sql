-- 
CREATE USER competitor WITH PASSWORD '123rockpaperscissor';
DROP DATABASE IF EXISTS rockpaperscissor;

CREATE DATABASE rockpaperscissor WITH OWNER competitor;

\c rockpaperscissor

CREATE TABLE "games" (
  "game_matchId" serial,
  "gameId" serial PRIMARY KEY,
  "gameCreatedOn" timestamp,
  "gamePlayerAChoice_codeId" integer,
  "gamePlayerBChoice_codeId" integer
);

CREATE TABLE "matches" (
  "match_sessionId" integer,
  "matchId" serial PRIMARY KEY,
  "matchCreatedOn" timestamp,
  "matchStatus_matchStatusId" integer
);

CREATE TABLE "match_statuses" (
  "matchStatusId" serial PRIMARY KEY,
  "matchStatusValue" varchar(100) UNIQUE,
  "matchStatusIsValid" boolean
);

CREATE TABLE "sessions" (
  "sessionId" serial PRIMARY KEY,
  "sessionCreatedOn" timestamp,
  "sessionAuthor" varchar(100)
);

ALTER TABLE "games" ADD FOREIGN KEY ("game_matchId") REFERENCES "matches" ("match_sessionId");
ALTER TABLE "matches" ADD FOREIGN KEY ("match_sessionId") REFERENCES "sessions" ("sessionId");
ALTER TABLE "matches" ADD FOREIGN KEY ("matchStatus_matchStatusId") REFERENCES "match_statuses" ("matchStatusId");


GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to competitor;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to competitor;
