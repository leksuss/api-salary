--
-- PostgreSQL database dump
--

-- Dumped from database version 13.15 (Debian 13.15-1.pgdg120+1)
-- Dumped by pg_dump version 13.15 (Debian 13.15-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, full_name, email, password) FROM stdin;
1	Ivan	123@123.ru	$2b$12$QIZGFv3jRUPLgrWj/gAzsuQwwFomnaTQpdUoHc7xQT/a3By4Hu.q6
2	Andrey	456@456.ru	$2b$12$HoX7pO.wYmAdLABQ/GxA8eQRxzfRmP8GPNUg/TyW1xstTqq0/ov/G
3	Boris	789@789.ru	$2b$12$RiR9/Bw3DcPfS0iMV2QVAOmt6JQ4ZlGtPxEnF6XDtrUqg/j2nKMjG
\.


--
-- Data for Name: salary; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.salary (id, user_id, amount, date_increase) FROM stdin;
1	1	45000	2024-05-30
2	2	146000	2024-06-28
3	3	91000	2024-06-13
\.


--
-- Name: salary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.salary_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

