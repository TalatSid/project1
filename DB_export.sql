-- Adminer 4.6.3-dev PostgreSQL dump

\connect "dd607mqt4i8gnt";

DROP TABLE IF EXISTS "location";
DROP SEQUENCE IF EXISTS location_sgk_location_id_seq;
CREATE SEQUENCE location_sgk_location_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."location" (
    "sgk_location_id" integer DEFAULT nextval('location_sgk_location_id_seq') NOT NULL,
    "zip_code" character varying NOT NULL,
    "city" character varying NOT NULL,
    "state" character varying NOT NULL,
    "latitude" numeric(8,6) NOT NULL,
    "longitude" numeric(9,6) NOT NULL,
    "population" integer NOT NULL,
    CONSTRAINT "location_sgk_location_id" PRIMARY KEY ("sgk_location_id"),
    CONSTRAINT "location_zip_code" UNIQUE ("zip_code")
) WITH (oids = false);

CREATE INDEX "idx_location_zip_code" ON "public"."location" USING btree ("zip_code");


DROP TABLE IF EXISTS "reg_user";
DROP SEQUENCE IF EXISTS reg_user_sgk_user_id_seq;
CREATE SEQUENCE reg_user_sgk_user_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."reg_user" (
    "sgk_user_id" integer DEFAULT nextval('reg_user_sgk_user_id_seq') NOT NULL,
    "login_name" character varying(15) NOT NULL,
    "login_pswd" character varying NOT NULL,
    "user_f_name" character varying NOT NULL,
    "user_l_name" character varying NOT NULL,
    "user_email" character varying NOT NULL,
    CONSTRAINT "reg_user_login_name" UNIQUE ("login_name"),
    CONSTRAINT "reg_user_sgk_user_id" PRIMARY KEY ("sgk_user_id"),
    CONSTRAINT "reg_user_user_email" UNIQUE ("user_email")
) WITH (oids = false);

CREATE INDEX "idx_reg_user_login_name" ON "public"."reg_user" USING btree ("login_name");


DROP TABLE IF EXISTS "test";
CREATE TABLE "public"."test" (
    "col1" integer
) WITH (oids = false);


DROP TABLE IF EXISTS "user_activity";
CREATE TABLE "public"."user_activity" (
    "sgk_user_id" integer NOT NULL,
    "sgk_session_id" integer NOT NULL,
    "sgk_location_id" integer NOT NULL,
    "comment" text,
    "appr_flag" integer NOT NULL,
    CONSTRAINT "idx_user_activity_sgk_user_id" PRIMARY KEY ("sgk_user_id", "sgk_session_id", "sgk_location_id"),
    CONSTRAINT "user_activity_sgk_location_id_fkey" FOREIGN KEY (sgk_location_id) REFERENCES location(sgk_location_id) ON UPDATE CASCADE ON DELETE CASCADE NOT DEFERRABLE,
    CONSTRAINT "user_activity_sgk_session_id_fkey" FOREIGN KEY (sgk_session_id) REFERENCES user_session(sgk_session_id) ON UPDATE CASCADE ON DELETE CASCADE NOT DEFERRABLE,
    CONSTRAINT "user_activity_sgk_user_id_fkey" FOREIGN KEY (sgk_user_id) REFERENCES reg_user(sgk_user_id) ON UPDATE CASCADE ON DELETE CASCADE NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "user_session";
DROP SEQUENCE IF EXISTS user_session_sgk_session_id_seq;
CREATE SEQUENCE user_session_sgk_session_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."user_session" (
    "sgk_session_id" integer DEFAULT nextval('user_session_sgk_session_id_seq') NOT NULL,
    "session_start_time" timestamp NOT NULL,
    "session_end_time" timestamp,
    "session_active_flag" integer NOT NULL,
    "sgk_user_id" integer NOT NULL,
    CONSTRAINT "user_session_sgk_session_id" PRIMARY KEY ("sgk_session_id"),
    CONSTRAINT "user_session_sgk_user_id_fkey" FOREIGN KEY (sgk_user_id) REFERENCES reg_user(sgk_user_id) ON UPDATE CASCADE ON DELETE CASCADE NOT DEFERRABLE
) WITH (oids = false);

CREATE INDEX "user_session_sgk_user_id" ON "public"."user_session" USING btree ("sgk_user_id");


-- 2018-07-12 20:16:28.348818+00
