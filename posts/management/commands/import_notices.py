from typing import Any
from playwright.sync_api import sync_playwright
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        with sync_playwright() as p:
            navegador = p.chromium.launch(headless=False)
            contexto = navegador.new_context()
            pagina = contexto.new_page()
            pagina.goto("https://draft5.gg/")
            pagina.wait_for_selector('.NewsCard__Title-sc-3os0ad-0.lnRqvG')
            noticias = pagina.query_selector_all('.NewsCard__Title-sc-3os0ad-0.lnRqvG')
            for noticia in noticias:
                titulo = noticia.text_content().strip()
                pagina_postagem = contexto.new_page()
                pagina_postagem.goto("http://127.0.0.1:8000/lista")
                pagina_postagem.click('text="Usuário"')
                pagina_postagem.click('text="Logar-se"')
                pagina_postagem.locator('#id_username').fill("adm123")
                pagina_postagem.locator('#id_password').fill("admin123")
                pagina_postagem.click('.login100-form-btn')
                pagina_postagem.goto("http://127.0.0.1:8000/lista")
                pagina_postagem.click('text="Criar postagem"')
                pagina_postagem.wait_for_selector('#Input1')
                pagina_postagem.locator('#Input1').fill(titulo)
                pagina_postagem.locator('#Textarea1').fill("gerado por ia")
                pagina_postagem.click('button[type="submit"]')
                pagina_postagem.goto("http://127.0.0.1:8000/lista")
                pagina_postagem.click('text="LOGOUT"')
                pagina_postagem.close()
            navegador.close()
        self.stdout.write(self.style.SUCCESS('NOTICIAS IMPORTADAS COM SUCESSO!'))