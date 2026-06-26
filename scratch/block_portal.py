import os

# Files to modify
portal_files = [
    r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\portal-cancilleria.html",
    r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\code.html"
]

template_file = r"c:\Users\Paul\Desktop\Pagina-Arquidiocesis-main\stitch_arquidi_cesis_de_maracaibo_digital\portal_de_sacerdotes_arquidi_cesis_de_maracaibo\code.html"

# Replacement block for portal-cancilleria.html and code.html
target_portal = """        <!-- 1. VIEW: LOGIN -->
        <div id="view-login" class="view active">
            <div class="glass-panel max-w-md w-full p-10 rounded-2xl shadow-2xl border border-outline-variant/30 text-center mx-auto animate-fadeIn">
                <div class="mb-6">
                    <div class="mx-auto w-28 h-28 rounded-full shadow-lg border-4 border-gold-antique/20 overflow-hidden bg-white flex items-center justify-center p-2">
                        <img src="img/logo-arquidiocesis.webp" alt="Escudo Curia" class="w-full h-full object-contain" onerror="this.src='https://placehold.co/70x70/00235B/FFCC00?text=A'">
                    </div>
                </div>
                <h2 class="font-display text-[26px] font-bold text-crimson-deep mb-1 leading-tight">Portal de Cancillería</h2>
                <p class="text-slate-warm font-label text-[13px] tracking-wide mb-6">Plataforma Digital de Trámites e Iglesia Metropolitana</p>
                



                <div class="flex border-b border-outline-variant/30 mb-5 justify-center">
                    <button type="button" id="tab-login-priest" onclick="setLoginType('priest')" class="px-5 py-2 font-label text-[14px] font-bold border-b-2 border-crimson-deep text-crimson-deep transition-all">Sacerdotes / Curia</button>
                    <button type="button" id="tab-login-parish" onclick="setLoginType('parish')" class="px-5 py-2 font-label text-[14px] font-bold border-b-2 border-transparent text-slate-warm hover:text-crimson-deep transition-all">Parroquias</button>
                </div>

                <form id="form-login" class="space-y-5 text-left" onsubmit="event.preventDefault(); handleLogin(event)">
                    <div id="container-login-email">
                        <label for="login-email" class="font-label text-[13px] font-bold text-slate-warm block mb-1.5">Correo Electrónico</label>
                        <input type="email" id="login-email" class="w-full bg-warm-ivory/50 border-b-2 border-outline-variant focus:border-crimson-deep focus:ring-0 outline-none px-4 py-3 transition-colors font-body text-[14px] rounded-t-lg" placeholder="Ej. pauldavid2809@gmail.com" required>
                    </div>
                    <div id="container-login-parish" style="display: none;" class="relative">
                        <label for="login-parish-search" class="font-label text-[13px] font-bold text-slate-warm block mb-1.5">Seleccione su Parroquia</label>
                        <div class="relative">
                            <input type="text" id="login-parish-search" class="w-full bg-warm-ivory/50 border-b-2 border-outline-variant focus:border-crimson-deep focus:ring-0 outline-none px-4 py-3 pr-10 transition-colors font-body text-[14px] rounded-t-lg cursor-pointer" placeholder="Escriba para buscar o seleccione..." autocomplete="off">
                            <button type="button" id="btn-toggle-parish-dropdown" class="absolute inset-y-0 right-0 flex items-center pr-3 text-slate-warm/70 hover:text-crimson-deep transition-colors">
                                <i class="ti ti-chevron-down text-[18px]"></i>
                            </button>
                        </div>
                        <input type="hidden" id="login-parish" value="">
                        
                        <!-- Dropdown list -->
                        <div id="login-parish-dropdown" class="absolute z-[100] left-0 right-0 mt-1 max-h-60 overflow-y-auto bg-white border border-outline-variant/30 rounded-lg shadow-xl hidden divide-y divide-slate-100">
                            <!-- Items populated dynamically -->
                        </div>
                    </div>
                    <div>
                        <label for="login-password" class="font-label text-[13px] font-bold text-slate-warm block mb-1.5">Contraseña</label>
                        <input type="password" id="login-password" class="w-full bg-warm-ivory/50 border-b-2 border-outline-variant focus:border-crimson-deep focus:ring-0 outline-none px-4 py-3 transition-colors font-body text-[14px] rounded-t-lg" placeholder="••••••••" required>
                    </div>
                    <button type="submit" id="btn-login-submit" class="w-full bg-crimson-deep text-white py-3.5 rounded-xl font-bold font-label text-[14px] hover:bg-primary hover:shadow-lg active:scale-95 transition-all uppercase tracking-wider flex items-center justify-center gap-2">
                        <i class="ti ti-login text-[18px]"></i> Ingresar al Portal
                    </button>
                </form>
                
                <div class="mt-6 pt-5 border-t border-outline-variant/30 flex flex-col gap-3 text-center">
                    <a href="#" id="link-forgot-password" onclick="switchView('view-forgot')" class="text-slate-warm hover:text-crimson-deep font-label text-[13px] transition-colors font-medium">¿Olvidó su contraseña? Restablézcala con su correo</a>
                    <a href="cancilleria.html" class="text-slate-warm hover:text-crimson-deep font-label text-[13px] transition-colors font-medium flex items-center justify-center gap-1">
                        <i class="ti ti-arrow-left"></i> Volver a Cancillería
                    </a>
                </div>
            </div>
        </div>"""

replacement_portal = """        <!-- 1. VIEW: LOGIN (BLOCKED) -->
        <div id="view-login" class="view active">
            <div class="glass-panel max-w-md w-full p-10 rounded-2xl shadow-2xl border border-outline-variant/30 text-center mx-auto animate-fadeIn">
                <div class="mb-6">
                    <div class="mx-auto w-24 h-24 rounded-full bg-gold-antique/10 border-4 border-gold-antique/20 overflow-hidden flex items-center justify-center">
                        <span class="material-symbols-outlined text-[42px] text-gold-antique">hourglass_empty</span>
                    </div>
                </div>
                <h2 class="font-display text-[26px] font-bold text-crimson-deep mb-2 leading-tight">Próximamente</h2>
                <p class="text-slate-warm font-label text-[14px] leading-relaxed mb-8">
                    El Portal Digital de Cancillería se encuentra actualmente en fase de desarrollo y estará disponible próximamente para todos los sacerdotes, curia y parroquias de nuestra Arquidiócesis.
                </p>
                <div class="space-y-4">
                    <a href="index.html" class="w-full bg-crimson-deep text-white py-3.5 rounded-xl font-bold font-label text-[14px] hover:bg-primary hover:shadow-lg active:scale-95 transition-all uppercase tracking-wider flex items-center justify-center gap-2">
                        Regresar al Inicio
                    </a>
                    <a href="cancilleria.html" class="w-full border-2 border-outline-variant text-slate-warm py-3 rounded-xl font-bold font-label text-[14px] hover:bg-slate-50 active:scale-95 transition-all uppercase tracking-wider flex items-center justify-center gap-2">
                        Volver a Cancillería
                    </a>
                </div>
            </div>
        </div>"""

# Replacement block for portal_de_sacerdotes_arquidi_cesis_de_maracaibo/code.html
target_template = """<!-- View: Login (Initial State) -->
<section class="flex items-center justify-center min-h-[614px] fade-in-up" id="view-login">
<div class="glass-panel max-w-md w-full p-10 rounded-2xl shadow-2xl border border-outline-variant/30 text-center">
<div class="mb-8">
<div class="mx-auto w-32 h-32 rounded-full shadow-lg border-4 border-gold-antique/20 overflow-hidden bg-white flex items-center justify-center">
<img alt="Logo" class="w-full h-full object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAyq1w6TZPeCuHN8dv5mHj7D2A4jRRidRR6AbBerGk5ap3mWSKrm2pCj7jBGPKJCfIMGyDZz4SXi4D0DjxM_hDcjLpm9pxBnevIeRfwvA20Bp0sFWWOXIugNtkYdPFl2KN8DcU-wI40_gDXNO8NIZk7ajq1T76yBrV2vHG5d7Lq-1TZWOYAI7dbhhrvb-ku_XvHr6ycGQIszMDwzBcGcAsbgWTjwSbydSLM586qqCGNvNc54ChkwBJS2huUsmu01vbJkw">
</div>
</div>
<h1 class="font-headline-md text-headline-md text-crimson-deep mb-2">Portal de Sacerdotes</h1>
<p class="text-slate-warm font-label-md text-label-md mb-8">Plataforma Digital de la Iglesia Metropolitana</p>
<form class="space-y-6 text-left" onsubmit="handleLogin(event)">
<div>
<label class="font-label-md text-label-md text-on-surface-variant block mb-2 font-semibold">Correo Institucional</label>
<input class="w-full bg-warm-ivory border-b-2 border-outline-variant focus:border-crimson-deep outline-none px-4 py-3 transition-colors font-body-md" id="login-email" placeholder="ejemplo@arquimcbo.org" required="" type="email">
</div>
<div>
<label class="font-label-md text-label-md text-on-surface-variant block mb-2 font-semibold">Contraseña</label>
<input class="w-full bg-warm-ivory border-b-2 border-outline-variant focus:border-crimson-deep outline-none px-4 py-3 transition-colors font-body-md" id="login-pass" placeholder="••••••••" required="" type="password">
</div>
<button class="w-full bg-crimson-deep text-on-primary py-4 rounded-xl font-bold font-label-md text-label-md hover:shadow-lg active:scale-95 transition-all uppercase tracking-wider" type="submit">
                        Ingresar al Portal
                    </button>
</form>
<div class="mt-8 pt-6 border-t border-outline-variant/30">
<a class="text-slate-warm hover:text-crimson-deep font-label-md text-label-md transition-colors" href="#">¿Olvidó sus credenciales?</a>
</div>
</div>
</section>"""

replacement_template = """<!-- View: Login (BLOCKED) -->
<section class="flex items-center justify-center min-h-[614px] fade-in-up" id="view-login">
<div class="glass-panel max-w-md w-full p-10 rounded-2xl shadow-2xl border border-outline-variant/30 text-center">
<div class="mb-8">
<div class="mx-auto w-24 h-24 rounded-full bg-gold-antique/10 border-4 border-gold-antique/20 overflow-hidden flex items-center justify-center">
<span class="material-symbols-outlined text-[42px] text-gold-antique">hourglass_empty</span>
</div>
</div>
<h1 class="font-headline-md text-headline-md text-crimson-deep mb-2">Próximamente</h1>
<p class="text-slate-warm font-label-md text-label-md mb-8">El Portal Digital de Sacerdotes se encuentra actualmente en desarrollo y estará disponible próximamente.</p>
<div class="space-y-4">
<a href="index.html" class="w-full bg-crimson-deep text-white py-3.5 rounded-xl font-bold font-label-md text-label-md hover:shadow-lg active:scale-95 transition-all uppercase tracking-wider flex items-center justify-center gap-2">
                        Regresar al Inicio
                    </a>
</div>
</div>
</section>"""

# Process portal-cancilleria.html and code.html
for p in portal_files:
    if os.path.exists(p):
        print(f"Modifying {p}")
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace normal login with blocked login
        # We search with normalized line endings
        norm_content = content.replace('\\r\\n', '\\n')
        norm_target = target_portal.replace('\\r\\n', '\\n')
        norm_replacement = replacement_portal.replace('\\r\\n', '\\n')
        
        if norm_target in norm_content:
            new_content = norm_content.replace(norm_target, norm_replacement)
            with open(p, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Successfully blocked.")
        else:
            # Fallback direct replacement
            new_content = content.replace(target_portal, replacement_portal)
            if new_content != content:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print("Successfully blocked (fallback).")
            else:
                print("Target not found. Doing manual search...")
                # Let's try finding a substring
                if "tab-login-priest" in content:
                    print("Found 'tab-login-priest', replacing from view-login start to end...")
                    start_idx = content.find('<!-- 1. VIEW: LOGIN -->')
                    end_idx = content.find('<!-- 2. VIEW: PASSWORD RECOVERY -->')
                    if start_idx != -1 and end_idx != -1:
                        new_content = content[:start_idx] + replacement_portal + "\n\n        " + content[end_idx:]
                        with open(p, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        print("Successfully blocked manually.")
                    else:
                        print("Could not find view indices.")
                else:
                    print("Substring tab-login-priest not found.")

# Process template file
if os.path.exists(template_file):
    print(f"Modifying template: {template_file}")
    with open(template_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    norm_content = content.replace('\\r\\n', '\\n')
    norm_target = target_template.replace('\\r\\n', '\\n')
    norm_replacement = replacement_template.replace('\\r\\n', '\\n')
    
    if norm_target in norm_content:
        new_content = norm_content.replace(norm_target, norm_replacement)
        with open(template_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Template successfully blocked.")
    else:
        new_content = content.replace(target_template, replacement_template)
        if new_content != content:
            with open(template_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Template successfully blocked (fallback).")
        else:
            print("Template target not found. Doing manual search...")
            start_idx = content.find('<!-- View: Login (Initial State) -->')
            end_idx = content.find('<!-- View: Priest Dashboard (Hidden by default) -->')
            if start_idx != -1 and end_idx != -1:
                new_content = content[:start_idx] + replacement_template + "\n" + content[end_idx:]
                with open(template_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print("Template successfully blocked manually.")
            else:
                print("Could not find template view indices.")
else:
    print("Template file not found.")
