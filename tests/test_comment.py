#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import pytest

import dhtmlparser

from abclinuxuapi import Comment


# Fixtures ====================================================================
@pytest.fixture
def reg_header():
    return dhtmlparser.parseString("""    <div class="ds_hlavicka" id="9">
        <div class="ds_reseni" style="display:none">
        </div>


        11.2. 15:21

<a href="/lide/manasekp">manasekp</a>             | skóre: 27
             | blog: <a href="/blog/manasekp">manasekp</a>
             | Brno

        <br>

            <span class="ds_control_sbalit2" id="comment9_toggle2">
                <a onClick="schovej_vlakno(9)" title="Schová nebo rozbalí celé vlákno">Rozbalit</a>
                <a onClick="rozbal_vse(9)" title="Schová nebo rozbalí vše pod tímto komentářem">Rozbalit vše</a>
            </span>

        Re: Bolest proxy


            <div id="comment9_controls">
                
                <a href="/blog/EditDiscussion/400959;jsessionid=kufis2spplnh6gu671mxqe2j?action=add&amp;dizId=210591&amp;threadId=9">Odpovědět</a>
                    | <a onClick="schovej_vlakno(9)" id="comment9_toggle1" title="Schová nebo rozbalí celé vlákno" class="ds_control_sbalit3">Sbalit</a>
                    | <a href="#2" title="Odkaz na komentář o jednu úroveň výše">Výše</a>
                    | <a href="#9" title="Přímá adresa na tento komentář">Link</a>
                    | <a href="/EditUser;jsessionid=kufis2spplnh6gu671mxqe2j?action=toBlacklist&amp;bUid=9480&amp;url=/blog/show/400959#9" title="Přidá autora na seznam blokovaných uživatelů">Blokovat</a>
                | <a href="/blog/EditRequest/400959;jsessionid=kufis2spplnh6gu671mxqe2j?action=comment&amp;threadId=9" title="Žádost o přesun diskuse, stížnost na komentář">Admin</a>
            </div>

    </div>""").find("div")[0]


@pytest.fixture
def unreg_header():
    return dhtmlparser.parseString("""    <div class="ds_hlavicka" id="3">
        <div class="ds_reseni" style="display:none">
        </div>


        10.2. 21:53

               Tomáškova máma

        <br>

            <span class="ds_control_sbalit2" id="comment3_toggle2">
                <a onClick="schovej_vlakno(3)" title="Schová nebo rozbalí celé vlákno">Rozbalit</a>
                <a onClick="rozbal_vse(3)" title="Schová nebo rozbalí vše pod tímto komentářem">Rozbalit vše</a>
            </span>

        Re: Bolest proxy


            <div id="comment3_controls">
                
                <a href="/blog/EditDiscussion/400959;jsessionid=kufis2spplnh6gu671mxqe2j?action=add&amp;dizId=210591&amp;threadId=3">Odpovědět</a>
                    | <a onClick="schovej_vlakno(3)" id="comment3_toggle1" title="Schová nebo rozbalí celé vlákno" class="ds_control_sbalit3">Sbalit</a>
                    
                    | <a href="#3" title="Přímá adresa na tento komentář">Link</a>
                    | <a href="/EditUser;jsessionid=kufis2spplnh6gu671mxqe2j?action=toBlacklist&amp;bName=Tom%C3%A1%C5%A1kova%20m%C3%A1ma&amp;url=/blog/show/400959#3" title="Přidá autora na seznam blokovaných uživatelů">Blokovat</a>
                | <a href="/blog/EditRequest/400959;jsessionid=kufis2spplnh6gu671mxqe2j?action=comment&amp;threadId=3" title="Žádost o přesun diskuse, stížnost na komentář">Admin</a>
            </div>

    </div>
    """).find("div")[0]


# Tests =======================================================================
def test_izolate_timestamp(unreg_header):
    ts = Comment._izolate_timestamp(unreg_header)

    assert ts == 1423601580


def test_izolate_timestamp_reg(reg_header):
    ts = Comment._izolate_timestamp(reg_header)

    assert ts == 1423664460


def test_izolate_name(unreg_header):
    username, registered = Comment._izolate_username(unreg_header)

    assert username == "Tomáškova máma"
    assert not registered


def test_izolate_name_reg(reg_header):
    username, registered = Comment._izolate_username(reg_header)

    assert username == "manasekp"
    assert registered
