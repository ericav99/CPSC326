
% ----------------------------------------------------------------------
% The following dataset was adapted from a similar one on the neo4j
% website:
% https://neo4j.com/graphgist/exploring-the-star-wars-social-network
% ----------------------------------------------------------------------


%
% Epsidoes and their names
%

movie(episode1,"Episode I: The Phantom Menace").
movie(episode2,"Episode II: Attack of the Clones").
movie(episode3,"Episode III: Revenge of the Sith").
movie(episode4,"Episode IV: A New Hope").
movie(episode5,"Episode V: The Empire Strikes Back").
movie(episode6,"Episode VI: Return of the Jedi").
movie(episode7,"Episode VII: The Force Awakens").

%
% characters (droid or person) and their names
%

droid(r2_d2,"R2-D2").
person(chewbacca,"CHEWBACCA").
droid(bb_8,"BB-8").
person(qui_gon,"QUI-GON").
person(nute_gunray,"NUTE GUNRAY").
person(pk_4,"PK-4").
person(tc_14,"TC-14").
person(obi_wan,"OBI-WAN").
person(dofine,"DOFINE").
person(rune,"RUNE").
person(tey_how,"TEY HOW").
person(emperor,"EMPEROR").
person(captain_panaka,"CAPTAIN PANAKA").
person(sio_bibble,"SIO BIBBLE").
person(jar_jar,"JAR JAR").
person(tarpals,"TARPALS").
person(boss_nass,"BOSS NASS").
person(padme,"PADME").
person(ric_olie,"RIC OLIE").
person(watto,"WATTO").
person(anakin,"ANAKIN").
person(sebulba,"SEBULBA").
person(jira,"JIRA").
person(shmi,"SHMI").
droid(c_3po,"C-3PO").
person(darth_maul,"DARTH MAUL").
person(kitster,"KITSTER").
person(wald,"WALD").
person(fode_beed,"FODE/BEED").
person(jabba,"JABBA").
person(greedo,"GREEDO").
person(valorum,"VALORUM").
person(mace_windu,"MACE WINDU").
person(ki_adi_mundi,"KI-ADI-MUNDI").
person(yoda,"YODA").
person(rabe,"RABE").
person(bail_organa,"BAIL ORGANA").
person(general_ceel,"GENERAL CEEL").
person(bravo_two,"BRAVO TWO").
person(bravo_three,"BRAVO THREE").
person(captain_typho,"CAPTAIN TYPHO").
person(senator_ask_aak,"SENATOR ASK AAK").
person(orn_free_taa,"ORN FREE TAA").
person(sola,"SOLA").
person(jobal,"JOBAL").
person(ruwee,"RUWEE").
person(taun_we,"TAUN WE").
person(lama_su,"LAMA SU").
person(boba_fett,"BOBA FETT").
person(jango_fett,"JANGO FETT").
person(owen,"OWEN").
person(beru,"BERU").
person(cliegg,"CLIEGG").
person(count_dooku,"COUNT DOOKU").
person(sun_rit,"SUN RIT").
person(poggle,"POGGLE").
person(plo_koon,"PLO KOON").
person(odd_ball,"ODD BALL").
person(general_grievous,"GENERAL GRIEVOUS").
person(fang_zar,"FANG ZAR").
person(mon_mothma,"MON MOTHMA").
person(giddean_danu,"GIDDEAN DANU").
person(clone_commander_gree,"CLONE COMMANDER GREE").
person(clone_commander_cody,"CLONE COMMANDER CODY").
person(tion_medon,"TION MEDON").
person(captain_antilles,"CAPTAIN ANTILLES").
person(darth_vader,"DARTH VADER").
person(luke,"LUKE").
person(camie,"CAMIE").
person(biggs,"BIGGS").
person(leia,"LEIA").
person(motti,"MOTTI").
person(tarkin,"TARKIN").
person(han,"HAN").
person(dodonna,"DODONNA").
person(gold_leader,"GOLD LEADER").
person(wedge,"WEDGE").
person(red_leader,"RED LEADER").
person(red_ten,"RED TEN").
person(gold_five,"GOLD FIVE").
person(rieekan,"RIEEKAN").
person(derlin,"DERLIN").
person(zev,"ZEV").
person(piett,"PIETT").
person(ozzel,"OZZEL").
person(dack,"DACK").
person(janson,"JANSON").
person(needa,"NEEDA").
person(lando,"LANDO").
person(jerjerrod,"JERJERROD").
person(bib_fortuna,"BIB FORTUNA").
person(boushh,"BOUSHH").
person(admiral_ackbar,"ADMIRAL ACKBAR").
person(lor_san_tekka,"LOR SAN TEKKA").
person(poe,"POE").
person(kylo_ren,"KYLO REN").
person(captain_phasma,"CAPTAIN PHASMA").
person(finn,"FINN").
person(unkar_plutt,"UNKAR PLUTT").
person(rey,"REY").
person(general_hux,"GENERAL HUX").
person(lieutenant_mitaka,"LIEUTENANT MITAKA").
person(bala_tik,"BALA-TIK").
person(snoke,"SNOKE").
person(maz,"MAZ").
person(snap,"SNAP").
person(admiral_statura,"ADMIRAL STATURA").
person(yolo_ziff,"YOLO ZIFF").
person(colonel_datoo,"COLONEL DATOO").
person(ello_asty,"ELLO ASTY").
person(jess,"JESS").
person(niv_lek,"NIV LEK").


% 
% Basic family tree information (main characters)
%

child_of(anakin,shmi).
child_of(padme,ruwee).
child_of(padme,jobal).
child_of(sola,ruwee).
child_of(sola,jobal).
child_of(ryoo,sola).
child_of(luke,padme).
child_of(luke,anakin).
child_of(leia,padme).
child_of(leia,anakin).
child_of(kylo_ren,leia).
child_of(kylo_ren,han). 


%
% social connection data on which characters have spoken to each other
%

speaks_with(chewbacca,r2_d2).
speaks_with(bb_8,r2_d2).
speaks_with(bb_8,chewbacca).
speaks_with(obi_wan,r2_d2).
speaks_with(padme,r2_d2).
speaks_with(qui_gon,r2_d2).
speaks_with(anakin,r2_d2).
speaks_with(r2_d2,watto).
speaks_with(c_3po,r2_d2).
speaks_with(kitster,r2_d2).
speaks_with(jabba,r2_d2).
speaks_with(emperor,r2_d2).
speaks_with(captain_typho,r2_d2).
speaks_with(beru,r2_d2).
speaks_with(owen,r2_d2).
speaks_with(bail_organa,r2_d2).
speaks_with(r2_d2,yoda).
speaks_with(luke,r2_d2).
speaks_with(leia,r2_d2).
speaks_with(captain_antilles,r2_d2).
speaks_with(biggs,r2_d2).
speaks_with(darth_vader,r2_d2).
speaks_with(han,r2_d2).
speaks_with(lando,r2_d2).
speaks_with(chewbacca,obi_wan).
speaks_with(c_3po,chewbacca).
speaks_with(chewbacca,luke).
speaks_with(chewbacca,han).
speaks_with(chewbacca,jabba).
speaks_with(chewbacca,leia).
speaks_with(chewbacca,darth_vader).
speaks_with(chewbacca,rieekan).
speaks_with(chewbacca,lando).
speaks_with(boba_fett,chewbacca).
speaks_with(chewbacca,finn).
speaks_with(chewbacca,rey).
speaks_with(bala_tik,chewbacca).
speaks_with(chewbacca,maz).
speaks_with(chewbacca,poe).
speaks_with(chewbacca,kylo_ren).
speaks_with(captain_phasma,chewbacca).
speaks_with(bb_8,poe).
speaks_with(bb_8,lor_san_tekka).
speaks_with(bb_8,rey).
speaks_with(bb_8,unkar_plutt).
speaks_with(bb_8,finn).
speaks_with(han,bb_8).			
speaks_with(bala_tik,bb_8).
speaks_with(bb_8,maz).
speaks_with(bb_8,leia).
speaks_with(bb_8,c_3po).
speaks_with(nute_gunray,qui_gon).
speaks_with(pk_4,tc_14).
speaks_with(obi_wan,tc_14).
speaks_with(qui_gon,tc_14).
speaks_with(obi_wan,qui_gon).
speaks_with(nute_gunray,tc_14).
speaks_with(dofine,nute_gunray).
speaks_with(dofine,tc_14).
speaks_with(nute_gunray,rune).
speaks_with(rune,tey_how).
speaks_with(nute_gunray,tey_how).
speaks_with(captain_panaka,emperor).
speaks_with(emperor,sio_bibble).
speaks_with(captain_panaka,sio_bibble).
speaks_with(jar_jar,qui_gon).
speaks_with(jar_jar,obi_wan).
speaks_with(jar_jar,tarpals).
speaks_with(boss_nass,qui_gon).
speaks_with(boss_nass,obi_wan).
speaks_with(boss_nass,jar_jar).
speaks_with(emperor,nute_gunray).
speaks_with(emperor,rune).
speaks_with(nute_gunray,sio_bibble).
speaks_with(jar_jar,sio_bibble).
speaks_with(captain_panaka,jar_jar).
speaks_with(qui_gon,sio_bibble).
speaks_with(captain_panaka,qui_gon).
speaks_with(captain_panaka,padme).
speaks_with(padme,qui_gon).
speaks_with(padme,sio_bibble).
speaks_with(captain_panaka,obi_wan).
speaks_with(obi_wan,ric_olie).
speaks_with(jar_jar,ric_olie).
speaks_with(qui_gon,ric_olie).
speaks_with(captain_panaka,ric_olie).
speaks_with(jar_jar,padme).
speaks_with(qui_gon,watto).
speaks_with(anakin,watto).
speaks_with(padme,watto).
speaks_with(anakin,qui_gon).
speaks_with(anakin,padme).
speaks_with(jar_jar,sebulba).
speaks_with(anakin,sebulba).
speaks_with(qui_gon,sebulba).
speaks_with(padme,sebulba).
speaks_with(anakin,jar_jar).
speaks_with(anakin,jira).
speaks_with(jira,qui_gon).
speaks_with(jira,padme).
speaks_with(anakin,shmi).
speaks_with(jar_jar,shmi).
speaks_with(qui_gon,shmi).
speaks_with(padme,shmi).
speaks_with(anakin,c_3po).
speaks_with(c_3po,padme).
speaks_with(obi_wan,sio_bibble).
speaks_with(darth_maul,emperor).
speaks_with(anakin,kitster).
speaks_with(anakin,wald).
speaks_with(kitster,wald).
speaks_with(jar_jar,kitster).
speaks_with(kitster,qui_gon).
speaks_with(jar_jar,wald).
speaks_with(qui_gon,wald).
speaks_with(anakin,obi_wan).
speaks_with(obi_wan,shmi).
speaks_with(c_3po,watto).
speaks_with(kitster,watto).
speaks_with(c_3po,qui_gon).
speaks_with(c_3po,kitster).
speaks_with(kitster,padme).
speaks_with(fode_beed,jabba).
speaks_with(jabba,shmi).
speaks_with(sebulba,shmi).
speaks_with(anakin,jabba).
speaks_with(jabba,jar_jar).
speaks_with(jabba,padme).
speaks_with(jabba,sebulba).
speaks_with(jabba,qui_gon).
speaks_with(fode_beed,jar_jar).
speaks_with(fode_beed,padme).
speaks_with(greedo,qui_gon).
speaks_with(anakin,greedo).
speaks_with(greedo,wald).
speaks_with(kitster,shmi).
speaks_with(anakin,captain_panaka).
speaks_with(anakin,ric_olie).
speaks_with(emperor,valorum).
speaks_with(emperor,jar_jar).
speaks_with(emperor,qui_gon).
speaks_with(jar_jar,valorum).
speaks_with(qui_gon,valorum).
speaks_with(mace_windu,qui_gon).
speaks_with(ki_adi_mundi,qui_gon).
speaks_with(qui_gon,yoda).
speaks_with(qui_gon,rabe).
speaks_with(ki_adi_mundi,mace_windu).
speaks_with(mace_windu,yoda).
speaks_with(anakin,mace_windu).
speaks_with(mace_windu,rabe).
speaks_with(ki_adi_mundi,yoda).
speaks_with(anakin,ki_adi_mundi).
speaks_with(ki_adi_mundi,rabe).
speaks_with(anakin,yoda).
speaks_with(rabe,yoda).
speaks_with(anakin,rabe).
speaks_with(bail_organa,emperor).
speaks_with(bail_organa,valorum).
speaks_with(obi_wan,yoda).
speaks_with(mace_windu,obi_wan).
speaks_with(ki_adi_mundi,obi_wan).
speaks_with(boss_nass,padme).
speaks_with(darth_maul,nute_gunray).
speaks_with(anakin,boss_nass).
speaks_with(boss_nass,captain_panaka).
speaks_with(obi_wan,padme).
speaks_with(emperor,general_ceel).
speaks_with(general_ceel,nute_gunray).
speaks_with(darth_maul,general_ceel).
speaks_with(darth_maul,rune).
speaks_with(bravo_two,ric_olie).
speaks_with(anakin,bravo_two).
speaks_with(general_ceel,jar_jar).
speaks_with(nute_gunray,padme).
speaks_with(dofine,tey_how).
speaks_with(bravo_three,bravo_two).
speaks_with(bravo_three,ric_olie).
speaks_with(anakin,bravo_three).
speaks_with(emperor,padme).
speaks_with(emperor,senator_ask_aak).
speaks_with(emperor,orn_free_taa).
speaks_with(orn_free_taa,senator_ask_aak).
speaks_with(emperor,mace_windu).
speaks_with(emperor,yoda).
speaks_with(emperor,ki_adi_mundi).
speaks_with(bail_organa,mace_windu).
speaks_with(bail_organa,yoda).
speaks_with(bail_organa,ki_adi_mundi).
speaks_with(captain_typho,jar_jar).
speaks_with(captain_typho,obi_wan).
speaks_with(anakin,captain_typho).
speaks_with(obi_wan,pk_4).
speaks_with(anakin,sio_bibble).
speaks_with(padme,sola).
speaks_with(anakin,sola).
speaks_with(jobal,sola).
speaks_with(ruwee,sola).
speaks_with(jobal,padme).
speaks_with(padme,ruwee).
speaks_with(anakin,jobal).
speaks_with(anakin,ruwee).
speaks_with(jobal,ruwee).
speaks_with(obi_wan,taun_we).
speaks_with(lama_su,taun_we).
speaks_with(lama_su,obi_wan).
speaks_with(boba_fett,taun_we).
speaks_with(boba_fett,jango_fett).
speaks_with(boba_fett,obi_wan).
speaks_with(jango_fett,taun_we).
speaks_with(jango_fett,obi_wan).
speaks_with(c_3po,owen).
speaks_with(beru,c_3po).
speaks_with(c_3po,cliegg).
speaks_with(anakin,owen).
speaks_with(anakin,beru).
speaks_with(anakin,cliegg).
speaks_with(beru,owen).
speaks_with(owen,padme).
speaks_with(cliegg,owen).
speaks_with(beru,padme).
speaks_with(beru,cliegg).
speaks_with(cliegg,padme).
speaks_with(bail_organa,obi_wan).
speaks_with(emperor,obi_wan).
speaks_with(obi_wan,senator_ask_aak).
speaks_with(bail_organa,senator_ask_aak).
speaks_with(bail_organa,jar_jar).
speaks_with(senator_ask_aak,yoda).
speaks_with(jar_jar,yoda).
speaks_with(mace_windu,senator_ask_aak).
speaks_with(jar_jar,mace_windu).
speaks_with(jar_jar,senator_ask_aak).
speaks_with(mace_windu,padme).
speaks_with(jar_jar,orn_free_taa).
speaks_with(count_dooku,padme).
speaks_with(count_dooku,jango_fett).
speaks_with(poggle,sun_rit).
speaks_with(nute_gunray,sun_rit).
speaks_with(nute_gunray,poggle).
speaks_with(obi_wan,sun_rit).
speaks_with(obi_wan,poggle).
speaks_with(nute_gunray,obi_wan).
speaks_with(count_dooku,obi_wan).
speaks_with(anakin,sun_rit).
speaks_with(anakin,poggle).
speaks_with(anakin,nute_gunray).
speaks_with(anakin,count_dooku).
speaks_with(padme,sun_rit).
speaks_with(count_dooku,sun_rit).
speaks_with(padme,poggle).
speaks_with(count_dooku,poggle).
speaks_with(count_dooku,nute_gunray).
speaks_with(count_dooku,mace_windu).
speaks_with(ki_adi_mundi,plo_koon).
speaks_with(count_dooku,yoda).
speaks_with(padme,yoda).
speaks_with(count_dooku,emperor).
speaks_with(obi_wan,odd_ball).
speaks_with(anakin,odd_ball).
speaks_with(anakin,emperor).
speaks_with(general_grievous,obi_wan).
speaks_with(anakin,general_grievous).
speaks_with(anakin,bail_organa).
speaks_with(c_3po,obi_wan).
speaks_with(c_3po,emperor).
speaks_with(bail_organa,c_3po).
speaks_with(bail_organa,padme).
speaks_with(bail_organa,fang_zar).
speaks_with(bail_organa,mon_mothma).
speaks_with(bail_organa,giddean_danu).
speaks_with(fang_zar,padme).
speaks_with(fang_zar,mon_mothma).
speaks_with(fang_zar,giddean_danu).
speaks_with(mon_mothma,padme).
speaks_with(giddean_danu,padme).
speaks_with(giddean_danu,mon_mothma).
speaks_with(captain_typho,padme).
speaks_with(c_3po,captain_typho).
speaks_with(clone_commander_gree,yoda).
speaks_with(clone_commander_cody,obi_wan).
speaks_with(obi_wan,tion_medon).
speaks_with(general_grievous,nute_gunray).
speaks_with(anakin,clone_commander_cody).
speaks_with(clone_commander_cody,mace_windu).
speaks_with(clone_commander_cody,yoda).
speaks_with(bail_organa,captain_antilles).
speaks_with(bail_organa,qui_gon).
speaks_with(c_3po,yoda).
speaks_with(darth_vader,emperor).
speaks_with(c_3po,captain_antilles).
speaks_with(camie,luke).
speaks_with(biggs,camie).
speaks_with(biggs,luke).
speaks_with(darth_vader,leia).
speaks_with(beru,luke).
speaks_with(luke,owen).
speaks_with(c_3po,luke).
speaks_with(c_3po,leia).
speaks_with(leia,luke).
speaks_with(beru,leia).
speaks_with(luke,obi_wan).
speaks_with(leia,obi_wan).
speaks_with(motti,tarkin).
speaks_with(darth_vader,motti).
speaks_with(darth_vader,tarkin).
speaks_with(han,obi_wan).
speaks_with(han,luke).
speaks_with(greedo,han).
speaks_with(han,jabba).
speaks_with(c_3po,han).
speaks_with(leia,motti).
speaks_with(leia,tarkin).
speaks_with(han,leia).
speaks_with(darth_vader,obi_wan).
speaks_with(dodonna,gold_leader).
speaks_with(dodonna,wedge).
speaks_with(dodonna,luke).
speaks_with(gold_leader,wedge).
speaks_with(gold_leader,luke).
speaks_with(luke,wedge).
speaks_with(biggs,leia).
speaks_with(leia,red_leader).
speaks_with(luke,red_leader).
speaks_with(biggs,red_leader).
speaks_with(biggs,c_3po).
speaks_with(c_3po,red_leader).
speaks_with(red_leader,wedge).
speaks_with(gold_leader,red_leader).
speaks_with(biggs,wedge).
speaks_with(red_leader,red_ten).
speaks_with(biggs,gold_leader).
speaks_with(luke,red_ten).
speaks_with(han,rieekan).
speaks_with(leia,rieekan).
speaks_with(c_3po,derlin).
speaks_with(han,zev).
speaks_with(c_3po,rieekan).
speaks_with(ozzel,piett).
speaks_with(darth_vader,piett).
speaks_with(darth_vader,ozzel).
speaks_with(derlin,leia).
speaks_with(dack,luke).
speaks_with(janson,wedge).
speaks_with(luke,zev).
speaks_with(darth_vader,needa).
speaks_with(needa,piett).
speaks_with(luke,yoda).
speaks_with(boba_fett,piett).
speaks_with(boba_fett,darth_vader).
speaks_with(han,lando).
speaks_with(lando,leia).
speaks_with(c_3po,lando).
speaks_with(darth_vader,lando).
speaks_with(darth_vader,han).
speaks_with(boba_fett,lando).
speaks_with(boba_fett,c_3po).
speaks_with(c_3po,darth_vader).
speaks_with(boba_fett,han).
speaks_with(boba_fett,leia).
speaks_with(darth_vader,luke).
speaks_with(lando,luke).
speaks_with(darth_vader,jerjerrod).
speaks_with(bib_fortuna,c_3po).
speaks_with(c_3po,jabba).
speaks_with(jabba,luke).
speaks_with(boushh,jabba).
speaks_with(boushh,c_3po).
speaks_with(boushh,han).
speaks_with(boushh,leia).
speaks_with(bib_fortuna,luke).
speaks_with(bib_fortuna,jabba).
speaks_with(han,mon_mothma).
speaks_with(admiral_ackbar,han).
speaks_with(lando,mon_mothma).
speaks_with(admiral_ackbar,lando).
speaks_with(admiral_ackbar,mon_mothma).
speaks_with(c_3po,mon_mothma).
speaks_with(leia,mon_mothma).
speaks_with(luke,mon_mothma).
speaks_with(admiral_ackbar,c_3po).
speaks_with(admiral_ackbar,leia).
speaks_with(admiral_ackbar,luke).
speaks_with(emperor,luke).
speaks_with(lando,wedge).
speaks_with(admiral_ackbar,wedge).
speaks_with(anakin,darth_vader).
speaks_with(anakin,luke).
speaks_with(lor_san_tekka,poe).
speaks_with(kylo_ren,lor_san_tekka).
speaks_with(kylo_ren,poe).
speaks_with(captain_phasma,kylo_ren).
speaks_with(captain_phasma,lor_san_tekka).
speaks_with(captain_phasma,poe).
speaks_with(captain_phasma,finn).
speaks_with(general_hux,kylo_ren).
speaks_with(rey,unkar_plutt).
speaks_with(finn,poe).
speaks_with(general_hux,lieutenant_mitaka).
speaks_with(kylo_ren,lieutenant_mitaka).
speaks_with(captain_phasma,general_hux).
speaks_with(finn,rey).
speaks_with(han,rey).
speaks_with(finn,han).
speaks_with(bala_tik,han).
speaks_with(bala_tik,rey).
speaks_with(bala_tik,finn).
speaks_with(general_hux,snoke).
speaks_with(kylo_ren,snoke).
speaks_with(han,maz).
speaks_with(finn,maz).
speaks_with(maz,rey).
speaks_with(han,poe).
speaks_with(leia,poe).
speaks_with(finn,leia).
speaks_with(kylo_ren,rey).
speaks_with(poe,snap).
speaks_with(admiral_ackbar,poe).
speaks_with(c_3po,poe).
speaks_with(admiral_statura,poe).
speaks_with(han,snap).
speaks_with(admiral_ackbar,snap).
speaks_with(finn,snap).
speaks_with(leia,snap).
speaks_with(c_3po,snap).
speaks_with(admiral_statura,snap).
speaks_with(admiral_statura,han).
speaks_with(admiral_ackbar,finn).
speaks_with(admiral_ackbar,admiral_statura).
speaks_with(c_3po,finn).
speaks_with(admiral_statura,finn).
speaks_with(admiral_statura,leia).
speaks_with(admiral_statura,c_3po).
speaks_with(captain_phasma,han).
speaks_with(colonel_datoo,general_hux).
speaks_with(ello_asty,poe).
speaks_with(jess,snap).
speaks_with(han,kylo_ren).
speaks_with(finn,kylo_ren).
speaks_with(jess,niv_lek).
speaks_with(niv_lek,yolo_ziff).
speaks_with(niv_lek,poe).
speaks_with(niv_lek,ello_asty).
speaks_with(jess,yolo_ziff).
speaks_with(jess,poe).
speaks_with(ello_asty,jess).
speaks_with(poe,yolo_ziff).
speaks_with(ello_asty,yolo_ziff).
speaks_with(leia,rey).
speaks_with(luke,rey).

%
% Character appearances in specific movies
%

appears_in(r2_d2,episode1).
appears_in(r2_d2,episode2).
appears_in(r2_d2,episode3).
appears_in(r2_d2,episode4).
appears_in(r2_d2,episode5).
appears_in(r2_d2,episode6).
appears_in(r2_d2,episode7).
appears_in(chewbacca,episode4).
appears_in(chewbacca,episode5).
appears_in(chewbacca,episode6).
appears_in(chewbacca,episode7).
appears_in(bb_8,episode7).
appears_in(qui_gon,episode1).
appears_in(qui_gon,episode3).
appears_in(nute_gunray,episode1).
appears_in(nute_gunray,episode2).
appears_in(nute_gunray,episode3).
appears_in(pk_4,episode1).
appears_in(pk_4,episode2).
appears_in(tc_14,episode1).
appears_in(obi_wan,episode1).
appears_in(obi_wan,episode2).
appears_in(obi_wan,episode3).
appears_in(obi_wan,episode4).
appears_in(obi_wan,episode5).
appears_in(obi_wan,episode6).
appears_in(dofine,episode1).
appears_in(rune,episode1).
appears_in(tey_how,episode1).
appears_in(emperor,episode1).
appears_in(emperor,episode2).
appears_in(emperor,episode3).
appears_in(emperor,episode5).
appears_in(emperor,episode6).
appears_in(captain_panaka,episode1).
appears_in(sio_bibble,episode1).
appears_in(sio_bibble,episode2).
appears_in(jar_jar,episode1).
appears_in(jar_jar,episode2).
appears_in(jar_jar,episode3).
appears_in(tarpals,episode1).
appears_in(boss_nass,episode1).
appears_in(padme,episode1).
appears_in(padme,episode2).
appears_in(padme,episode3).
appears_in(ric_olie,episode1).
appears_in(watto,episode1).
appears_in(watto,episode2).
appears_in(anakin,episode1).
appears_in(anakin,episode2).
appears_in(anakin,episode3).
appears_in(anakin,episode6).
appears_in(sebulba,episode1).
appears_in(jira,episode1).
appears_in(shmi,episode1).
appears_in(shmi,episode2).
appears_in(c_3po,episode1).
appears_in(c_3po,episode2).
appears_in(c_3po,episode3).
appears_in(c_3po,episode4).
appears_in(c_3po,episode5).
appears_in(c_3po,episode6).
appears_in(c_3po,episode7).
appears_in(darth_maul,episode1).
appears_in(kitster,episode1).
appears_in(wald,episode1).
appears_in(fode_beed,episode1).
appears_in(jabba,episode1).
appears_in(jabba,episode4).
appears_in(jabba,episode6).
appears_in(greedo,episode1).
appears_in(greedo,episode4).
appears_in(valorum,episode1).
appears_in(mace_windu,episode1).
appears_in(mace_windu,episode2).
appears_in(mace_windu,episode3).
appears_in(ki_adi_mundi,episode1).
appears_in(ki_adi_mundi,episode2).
appears_in(yoda,episode1).
appears_in(yoda,episode2).
appears_in(yoda,episode3).
appears_in(yoda,episode5).
appears_in(yoda,episode6).
appears_in(rabe,episode1).
appears_in(bail_organa,episode1).
appears_in(bail_organa,episode2).
appears_in(bail_organa,episode3).
appears_in(general_ceel,episode1).
appears_in(bravo_two,episode1).
appears_in(bravo_three,episode1).
appears_in(captain_typho,episode2).
appears_in(captain_typho,episode3).
appears_in(senator_ask_aak,episode2).
appears_in(orn_free_taa,episode2).
appears_in(sola,episode2).
appears_in(jobal,episode2).
appears_in(ruwee,episode2).
appears_in(taun_we,episode2).
appears_in(lama_su,episode2).
appears_in(boba_fett,episode2).
appears_in(boba_fett,episode5).
appears_in(jango_fett,episode2).
appears_in(owen,episode2).
appears_in(owen,episode4).
appears_in(beru,episode2).
appears_in(beru,episode4).
appears_in(cliegg,episode2).
appears_in(count_dooku,episode2).
appears_in(count_dooku,episode3).
appears_in(sun_rit,episode2).
appears_in(poggle,episode2).
appears_in(plo_koon,episode2).
appears_in(plo_koon,episode3).
appears_in(odd_ball,episode3).
appears_in(general_grievous,episode3).
appears_in(fang_zar,episode3).
appears_in(mon_mothma,episode3).
appears_in(mon_mothma,episode6).
appears_in(giddean_danu,episode3).
appears_in(clone_commander_gree,episode3).
appears_in(clone_commander_cody,episode3).
appears_in(tion_medon,episode3).
appears_in(captain_antilles,episode3).
appears_in(darth_vader,episode3).
appears_in(darth_vader,episode4).
appears_in(darth_vader,episode5).
appears_in(darth_vader,episode6).
appears_in(luke,episode4).
appears_in(luke,episode5).
appears_in(luke,episode6).
appears_in(luke,episode7).
appears_in(camie,episode4).
appears_in(biggs,episode4).
appears_in(leia,episode4).
appears_in(leia,episode5).
appears_in(leia,episode6).
appears_in(leia,episode7).
appears_in(motti,episode4).
appears_in(tarkin,episode4).
appears_in(han,episode4).
appears_in(han,episode5).
appears_in(han,episode6).
appears_in(han,episode7).
appears_in(dodonna,episode4).
appears_in(gold_leader,episode4).
appears_in(wedge,episode4).
appears_in(wedge,episode5).
appears_in(wedge,episode6).
appears_in(red_leader,episode4).
appears_in(red_ten,episode4).
appears_in(gold_five,episode4).
appears_in(rieekan,episode5).
appears_in(derlin,episode5).
appears_in(zev,episode5).
appears_in(piett,episode5).
appears_in(piett,episode6).
appears_in(ozzel,episode5).
appears_in(dack,episode5).
appears_in(janson,episode5).
appears_in(needa,episode5).
appears_in(lando,episode5).
appears_in(lando,episode6).
appears_in(jerjerrod,episode6).
appears_in(bib_fortuna,episode6).
appears_in(boushh,episode6).
appears_in(admiral_ackbar,episode6).
appears_in(admiral_ackbar,episode7).
appears_in(lor_san_tekka,episode7).
appears_in(poe,episode7).
appears_in(kylo_ren,episode7).
appears_in(captain_phasma,episode7).
appears_in(finn,episode7).
appears_in(unkar_plutt,episode7).
appears_in(rey,episode7).
appears_in(general_hux,episode7).
appears_in(lieutenant_mitaka,episode7).
appears_in(bala_tik,episode7).
appears_in(snoke,episode7).
appears_in(maz,episode7).
appears_in(snap,episode7).
appears_in(admiral_statura,episode7).
appears_in(yolo_ziff,episode7).
appears_in(colonel_datoo,episode7).
appears_in(ello_asty,episode7).
appears_in(jess,episode7).
appears_in(niv_lek,episode7).
