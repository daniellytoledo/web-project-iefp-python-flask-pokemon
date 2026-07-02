from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.srv_pokemon_cards import tbl_cards, tbl_collections, tbl_stages, tbl_types, vw_cards_full_info



