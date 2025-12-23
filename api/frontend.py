from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["frontend"])


def get_base_styles():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');
    
    :root {
        --bg-primary: #0a0a0f;
        --bg-secondary: #12121a;
        --bg-card: #1a1a25;
        --bg-hover: #222230;
        --accent-primary: #6366f1;
        --accent-secondary: #8b5cf6;
        --accent-gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --border-color: rgba(99, 102, 241, 0.2);
        --success: #10b981;
        --error: #ef4444;
        --warning: #f59e0b;
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Outfit', sans-serif;
        background: var(--bg-primary);
        color: var(--text-primary);
        min-height: 100vh;
        overflow-x: hidden;
    }
    
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(ellipse at 20% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(168, 85, 247, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(236, 72, 153, 0.05) 0%, transparent 70%);
        pointer-events: none;
        z-index: -1;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .animate-fade { animation: fadeIn 0.5s ease-out forwards; }
    .animate-slide { animation: slideIn 0.5s ease-out forwards; }
    
    /* Form Elements */
    .form-group {
        margin-bottom: 1.5rem;
    }
    
    .form-label {
        display: block;
        font-size: 0.875rem;
        font-weight: 500;
        color: var(--text-secondary);
        margin-bottom: 0.5rem;
        letter-spacing: 0.025em;
    }
    
    .form-input {
        width: 100%;
        padding: 0.875rem 1rem;
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        color: var(--text-primary);
        font-size: 1rem;
        font-family: inherit;
        transition: all 0.3s ease;
    }
    
    .form-input:focus {
        outline: none;
        border-color: var(--accent-primary);
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    }
    
    .form-input::placeholder {
        color: var(--text-muted);
    }
    
    /* Buttons */
    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        padding: 0.875rem 1.5rem;
        font-size: 0.95rem;
        font-weight: 600;
        font-family: inherit;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    .btn-primary {
        background: var(--accent-gradient);
        color: white;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
    }
    
    .btn-secondary {
        background: var(--bg-card);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
    }
    
    .btn-secondary:hover {
        background: var(--bg-hover);
        border-color: var(--accent-primary);
    }
    
    .btn-danger {
        background: var(--error);
        color: white;
    }
    
    .btn-danger:hover {
        background: #dc2626;
    }
    
    .btn:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        transform: none !important;
    }
    
    .btn-full { width: 100%; }
    
    /* Cards */
    .card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
    }
    
    /* Messages */
    .message {
        padding: 1rem 1.25rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .message-success {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: var(--success);
    }
    
    .message-error {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        color: var(--error);
    }
    
    .hidden { display: none !important; }
    
    /* Spinner */
    .spinner {
        width: 20px;
        height: 20px;
        border: 2px solid transparent;
        border-top-color: currentColor;
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    """


def get_auth_page():
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Giriş Yap | PhotoFlow</title>
        <style>
            {get_base_styles()}
            
            .auth-wrapper {{
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 2rem;
            }}
            
            .auth-container {{
                width: 100%;
                max-width: 420px;
            }}
            
            .auth-logo {{
                text-align: center;
                margin-bottom: 2.5rem;
            }}
            
            .auth-logo h1 {{
                font-size: 2.5rem;
                font-weight: 700;
                background: var(--accent-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                letter-spacing: -0.02em;
            }}
            
            .auth-logo p {{
                color: var(--text-secondary);
                margin-top: 0.5rem;
                font-size: 1rem;
            }}
            
            .auth-card {{
                animation: fadeIn 0.6s ease-out;
            }}
            
            .auth-tabs {{
                display: flex;
                gap: 0.5rem;
                margin-bottom: 2rem;
                background: var(--bg-secondary);
                padding: 0.375rem;
                border-radius: 14px;
            }}
            
            .auth-tab {{
                flex: 1;
                padding: 0.75rem;
                text-align: center;
                border-radius: 10px;
                cursor: pointer;
                font-weight: 500;
                color: var(--text-secondary);
                transition: all 0.3s ease;
                border: none;
                background: transparent;
                font-family: inherit;
                font-size: 0.95rem;
            }}
            
            .auth-tab.active {{
                background: var(--accent-gradient);
                color: white;
                box-shadow: 0 2px 10px rgba(99, 102, 241, 0.3);
            }}
            
            .auth-tab:not(.active):hover {{
                color: var(--text-primary);
            }}
            
            .auth-form {{
                display: none;
            }}
            
            .auth-form.active {{
                display: block;
            }}
            
            .auth-divider {{
                display: flex;
                align-items: center;
                gap: 1rem;
                margin: 1.5rem 0;
                color: var(--text-muted);
                font-size: 0.85rem;
            }}
            
            .auth-divider::before,
            .auth-divider::after {{
                content: '';
                flex: 1;
                height: 1px;
                background: var(--border-color);
            }}
            
            .password-toggle {{
                position: relative;
            }}
            
            .password-toggle .toggle-btn {{
                position: absolute;
                right: 1rem;
                top: 50%;
                transform: translateY(-50%);
                background: none;
                border: none;
                color: var(--text-muted);
                cursor: pointer;
                padding: 0.25rem;
            }}
            
            .password-toggle .toggle-btn:hover {{
                color: var(--text-secondary);
            }}
            
            .auth-footer {{
                text-align: center;
                margin-top: 2rem;
                color: var(--text-secondary);
                font-size: 0.875rem;
            }}
            
            .auth-footer a {{
                color: var(--accent-primary);
                text-decoration: none;
                font-weight: 500;
            }}
            
            .auth-footer a:hover {{
                text-decoration: underline;
            }}
            
            .floating-shapes {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                overflow: hidden;
                z-index: -1;
            }}
            
            .shape {{
                position: absolute;
                border-radius: 50%;
                opacity: 0.1;
                animation: float 6s ease-in-out infinite;
            }}
            
            .shape-1 {{
                width: 300px;
                height: 300px;
                background: var(--accent-primary);
                top: -100px;
                left: -100px;
                animation-delay: 0s;
            }}
            
            .shape-2 {{
                width: 200px;
                height: 200px;
                background: var(--accent-secondary);
                bottom: -50px;
                right: -50px;
                animation-delay: 2s;
            }}
            
            .shape-3 {{
                width: 150px;
                height: 150px;
                background: #ec4899;
                top: 50%;
                right: 10%;
                animation-delay: 4s;
            }}
        </style>
    </head>
    <body>
        <div class="floating-shapes">
            <div class="shape shape-1"></div>
            <div class="shape shape-2"></div>
            <div class="shape shape-3"></div>
        </div>
        
        <div class="auth-wrapper">
            <div class="auth-container">
                <div class="auth-logo">
                    <h1>📸 PhotoFlow</h1>
                    <p>Anılarını paylaş, dünyayı keşfet</p>
                </div>
                
                <div class="card auth-card">
                    <div class="auth-tabs">
                        <button class="auth-tab active" data-tab="login">Giriş Yap</button>
                        <button class="auth-tab" data-tab="register">Kayıt Ol</button>
                    </div>
                    
                    <div id="message-container"></div>
                    
                    <!-- Login Form -->
                    <form id="login-form" class="auth-form active">
                        <div class="form-group">
                            <label class="form-label">E-posta Adresi</label>
                            <input type="email" name="username" class="form-input" placeholder="ornek@email.com" required>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Şifre</label>
                            <div class="password-toggle">
                                <input type="password" name="password" class="form-input" placeholder="••••••••" required>
                                <button type="button" class="toggle-btn" onclick="togglePassword(this)">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                                        <circle cx="12" cy="12" r="3"></circle>
                                    </svg>
                                </button>
                            </div>
                        </div>
                        
                        <button type="submit" class="btn btn-primary btn-full">
                            <span class="btn-text">Giriş Yap</span>
                            <span class="spinner hidden"></span>
                        </button>
                    </form>
                    
                    <!-- Register Form -->
                    <form id="register-form" class="auth-form">
                        <div class="form-group">
                            <label class="form-label">E-posta Adresi</label>
                            <input type="email" name="email" class="form-input" placeholder="ornek@email.com" required>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Şifre</label>
                            <div class="password-toggle">
                                <input type="password" name="password" class="form-input" placeholder="En az 8 karakter" minlength="8" required>
                                <button type="button" class="toggle-btn" onclick="togglePassword(this)">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                                        <circle cx="12" cy="12" r="3"></circle>
                                    </svg>
                                </button>
                            </div>
                        </div>
                        
                        <button type="submit" class="btn btn-primary btn-full">
                            <span class="btn-text">Hesap Oluştur</span>
                            <span class="spinner hidden"></span>
                        </button>
                    </form>
                </div>
                
                <div class="auth-footer">
                    <p>Devam ederek <a href="#">Kullanım Şartları</a>'nı kabul etmiş olursunuz.</p>
                </div>
            </div>
        </div>
        
        <script>
            // Tab switching
            var authTabs = document.querySelectorAll('.auth-tab');
            for (var i = 0; i < authTabs.length; i++) {{
                authTabs[i].addEventListener('click', function() {{
                    var allTabs = document.querySelectorAll('.auth-tab');
                    var allForms = document.querySelectorAll('.auth-form');
                    for (var j = 0; j < allTabs.length; j++) {{
                        allTabs[j].classList.remove('active');
                    }}
                    for (var k = 0; k < allForms.length; k++) {{
                        allForms[k].classList.remove('active');
                    }}
                    this.classList.add('active');
                    document.getElementById(this.dataset.tab + '-form').classList.add('active');
                    clearMessages();
                }});
            }}
            
            // Password toggle
            function togglePassword(btn) {{
                var input = btn.parentElement.querySelector('input');
                input.type = input.type === 'password' ? 'text' : 'password';
            }}
            
            // Show message
            function showMessage(message, type) {{
                if (!type) type = 'error';
                var container = document.getElementById('message-container');
                var icon = type === 'success' 
                    ? '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>'
                    : '<circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line>';
                container.innerHTML = '<div class="message message-' + type + '"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">' + icon + '</svg>' + message + '</div>';
            }}
            
            function clearMessages() {{
                document.getElementById('message-container').innerHTML = '';
            }}
            
            // Login form
            document.getElementById('login-form').addEventListener('submit', async function(e) {{
                e.preventDefault();
                var btn = e.target.querySelector('button[type="submit"]');
                var btnText = btn.querySelector('.btn-text');
                var spinner = btn.querySelector('.spinner');
                
                btn.disabled = true;
                btnText.textContent = 'Giris yapiliyor...';
                spinner.classList.remove('hidden');
                
                var formData = new FormData(e.target);
                
                try {{
                    var response = await fetch('/auth/jwt/login', {{
                        method: 'POST',
                        body: formData
                    }});
                    
                    if (response.ok) {{
                        var data = await response.json();
                        localStorage.setItem('access_token', data.access_token);
                        console.log('Token kaydedildi:', data.access_token);
                        showMessage('Giris basarili! Yonlendiriliyorsunuz...', 'success');
                        setTimeout(function() {{ window.location.href = '/app'; }}, 1000);
                    }} else {{
                        var errorData = await response.json();
                        showMessage(errorData.detail || 'Giris basarisiz. Lutfen bilgilerinizi kontrol edin.');
                    }}
                }} catch (error) {{
                    console.error('Login error:', error);
                    showMessage('Bir hata olustu. Lutfen tekrar deneyin.');
                }} finally {{
                    btn.disabled = false;
                    btnText.textContent = 'Giris Yap';
                    spinner.classList.add('hidden');
                }}
            }});
            
            // Register form
            document.getElementById('register-form').addEventListener('submit', async function(e) {{
                e.preventDefault();
                var btn = e.target.querySelector('button[type="submit"]');
                var btnText = btn.querySelector('.btn-text');
                var spinner = btn.querySelector('.spinner');
                
                btn.disabled = true;
                btnText.textContent = 'Hesap olusturuluyor...';
                spinner.classList.remove('hidden');
                
                var formData = new FormData(e.target);
                var data = {{
                    email: formData.get('email'),
                    password: formData.get('password')
                }};
                
                try {{
                    var response = await fetch('/auth/register', {{
                        method: 'POST',
                        headers: {{ 'Content-Type': 'application/json' }},
                        body: JSON.stringify(data)
                    }});
                    
                    if (response.ok) {{
                        showMessage('Hesabiniz olusturuldu! Simdi giris yapabilirsiniz.', 'success');
                        document.querySelector('[data-tab="login"]').click();
                    }} else {{
                        var errorData = await response.json();
                        showMessage(errorData.detail || 'Kayit basarisiz. Lutfen tekrar deneyin.');
                    }}
                }} catch (error) {{
                    console.error('Register error:', error);
                    showMessage('Bir hata olustu. Lutfen tekrar deneyin.');
                }} finally {{
                    btn.disabled = false;
                    btnText.textContent = 'Hesap Olustur';
                    spinner.classList.add('hidden');
                }}
            }});
            
            // Check if already logged in
            if (localStorage.getItem('access_token')) {{
                window.location.href = '/app';
            }}
        </script>
    </body>
    </html>
    """


def get_app_page():
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PhotoFlow | Ana Sayfa</title>
        <style>
            {get_base_styles()}
            
            /* Header */
            .header {{
                background: rgba(10, 10, 15, 0.8);
                backdrop-filter: blur(20px);
                border-bottom: 1px solid var(--border-color);
                position: sticky;
                top: 0;
                z-index: 100;
            }}
            
            .header-content {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 1rem 0;
            }}
            
            .logo {{
                font-size: 1.5rem;
                font-weight: 700;
                background: var(--accent-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            
            .header-actions {{
                display: flex;
                align-items: center;
                gap: 1rem;
            }}
            
            .user-menu {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
                padding: 0.5rem 1rem;
                background: var(--bg-card);
                border-radius: 50px;
                border: 1px solid var(--border-color);
            }}
            
            .user-avatar {{
                width: 36px;
                height: 36px;
                border-radius: 50%;
                background: var(--accent-gradient);
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 600;
                font-size: 0.875rem;
            }}
            
            .user-email {{
                font-size: 0.875rem;
                color: var(--text-secondary);
                max-width: 150px;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }}
            
            .logout-btn {{
                background: none;
                border: none;
                color: var(--text-muted);
                cursor: pointer;
                padding: 0.5rem;
                border-radius: 8px;
                transition: all 0.3s ease;
            }}
            
            .logout-btn:hover {{
                background: var(--bg-hover);
                color: var(--error);
            }}
            
            /* Main Layout */
            .main-content {{
                display: grid;
                grid-template-columns: 1fr 380px;
                gap: 2rem;
                padding: 2rem 0;
                min-height: calc(100vh - 80px);
            }}
            
            @media (max-width: 1024px) {{
                .main-content {{
                    grid-template-columns: 1fr;
                }}
                
                .sidebar {{
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    right: 0;
                    z-index: 100;
                    padding: 1rem;
                    background: rgba(10, 10, 15, 0.95);
                    backdrop-filter: blur(20px);
                    border-top: 1px solid var(--border-color);
                }}
            }}
            
            /* Feed */
            .feed-header {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: 1.5rem;
            }}
            
            .feed-title {{
                font-size: 1.75rem;
                font-weight: 700;
            }}
            
            .refresh-btn {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                color: var(--text-primary);
                padding: 0.75rem;
                border-radius: 12px;
                cursor: pointer;
                transition: all 0.3s ease;
            }}
            
            .refresh-btn:hover {{
                background: var(--bg-hover);
                border-color: var(--accent-primary);
            }}
            
            .refresh-btn.loading svg {{
                animation: spin 1s linear infinite;
            }}
            
            .feed-grid {{
                display: grid;
                gap: 1.5rem;
            }}
            
            /* Post Card */
            .post-card {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 20px;
                overflow: hidden;
                animation: fadeIn 0.5s ease-out;
            }}
            
            .post-header {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 1rem 1.25rem;
            }}
            
            .post-author {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }}
            
            .post-avatar {{
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: var(--accent-gradient);
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 600;
                font-size: 0.875rem;
            }}
            
            .post-author-info h4 {{
                font-size: 0.95rem;
                font-weight: 600;
            }}
            
            .post-author-info span {{
                font-size: 0.8rem;
                color: var(--text-muted);
            }}
            
            .post-menu {{
                position: relative;
            }}
            
            .post-menu-btn {{
                background: none;
                border: none;
                color: var(--text-muted);
                cursor: pointer;
                padding: 0.5rem;
                border-radius: 8px;
                transition: all 0.3s ease;
            }}
            
            .post-menu-btn:hover {{
                background: var(--bg-hover);
                color: var(--text-primary);
            }}
            
            .post-dropdown {{
                position: absolute;
                top: 100%;
                right: 0;
                background: var(--bg-secondary);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 0.5rem;
                min-width: 150px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
                z-index: 10;
                display: none;
            }}
            
            .post-dropdown.active {{
                display: block;
            }}
            
            .dropdown-item {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
                padding: 0.75rem 1rem;
                border-radius: 8px;
                cursor: pointer;
                font-size: 0.9rem;
                transition: all 0.2s ease;
                border: none;
                background: none;
                width: 100%;
                color: var(--text-primary);
                font-family: inherit;
            }}
            
            .dropdown-item:hover {{
                background: var(--bg-hover);
            }}
            
            .dropdown-item.danger {{
                color: var(--error);
            }}
            
            .post-media {{
                position: relative;
                background: var(--bg-primary);
            }}
            
            .post-media img,
            .post-media video {{
                width: 100%;
                max-height: 600px;
                object-fit: contain;
                display: block;
            }}
            
            .post-content {{
                padding: 1.25rem;
            }}
            
            .post-caption {{
                font-size: 0.95rem;
                line-height: 1.6;
                color: var(--text-secondary);
            }}
            
            .owner-badge {{
                display: inline-flex;
                align-items: center;
                gap: 0.375rem;
                padding: 0.25rem 0.625rem;
                background: rgba(99, 102, 241, 0.1);
                border: 1px solid rgba(99, 102, 241, 0.2);
                border-radius: 50px;
                font-size: 0.75rem;
                color: var(--accent-primary);
                font-weight: 500;
            }}
            
            /* Sidebar Upload */
            .sidebar {{
                position: sticky;
                top: 100px;
                height: fit-content;
            }}
            
            .upload-card {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 20px;
                padding: 1.5rem;
            }}
            
            .upload-card h3 {{
                font-size: 1.25rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }}
            
            .upload-dropzone {{
                border: 2px dashed var(--border-color);
                border-radius: 16px;
                padding: 2rem;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                margin-bottom: 1.5rem;
            }}
            
            .upload-dropzone:hover,
            .upload-dropzone.dragover {{
                border-color: var(--accent-primary);
                background: rgba(99, 102, 241, 0.05);
            }}
            
            .upload-dropzone svg {{
                width: 48px;
                height: 48px;
                color: var(--text-muted);
                margin-bottom: 1rem;
            }}
            
            .upload-dropzone p {{
                color: var(--text-secondary);
                font-size: 0.9rem;
            }}
            
            .upload-dropzone span {{
                color: var(--accent-primary);
                font-weight: 500;
            }}
            
            .upload-preview {{
                position: relative;
                margin-bottom: 1.5rem;
                border-radius: 12px;
                overflow: hidden;
                display: none;
            }}
            
            .upload-preview.active {{
                display: block;
            }}
            
            .upload-preview img,
            .upload-preview video {{
                width: 100%;
                max-height: 200px;
                object-fit: cover;
                display: block;
            }}
            
            .upload-preview .remove-btn {{
                position: absolute;
                top: 0.5rem;
                right: 0.5rem;
                width: 32px;
                height: 32px;
                background: rgba(0, 0, 0, 0.7);
                border: none;
                border-radius: 50%;
                color: white;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.3s ease;
            }}
            
            .upload-preview .remove-btn:hover {{
                background: var(--error);
            }}
            
            .upload-progress {{
                margin-bottom: 1rem;
                display: none;
            }}
            
            .upload-progress.active {{
                display: block;
            }}
            
            .progress-bar {{
                height: 6px;
                background: var(--bg-secondary);
                border-radius: 3px;
                overflow: hidden;
            }}
            
            .progress-fill {{
                height: 100%;
                background: var(--accent-gradient);
                border-radius: 3px;
                transition: width 0.3s ease;
                width: 0%;
            }}
            
            .progress-text {{
                font-size: 0.8rem;
                color: var(--text-muted);
                margin-top: 0.5rem;
                text-align: center;
            }}
            
            /* Empty State */
            .empty-state {{
                text-align: center;
                padding: 4rem 2rem;
                color: var(--text-secondary);
            }}
            
            .empty-state svg {{
                width: 80px;
                height: 80px;
                color: var(--text-muted);
                margin-bottom: 1.5rem;
                opacity: 0.5;
            }}
            
            .empty-state h3 {{
                font-size: 1.25rem;
                color: var(--text-primary);
                margin-bottom: 0.5rem;
            }}
            
            .empty-state p {{
                font-size: 0.95rem;
            }}
            
            /* Loading Skeleton */
            .skeleton {{
                background: linear-gradient(90deg, var(--bg-card) 25%, var(--bg-hover) 50%, var(--bg-card) 75%);
                background-size: 200% 100%;
                animation: shimmer 1.5s infinite;
                border-radius: 8px;
            }}
            
            .skeleton-post {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 20px;
                overflow: hidden;
            }}
            
            .skeleton-header {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
                padding: 1rem 1.25rem;
            }}
            
            .skeleton-avatar {{
                width: 40px;
                height: 40px;
                border-radius: 50%;
            }}
            
            .skeleton-text {{
                height: 12px;
                width: 120px;
            }}
            
            .skeleton-media {{
                height: 300px;
            }}
            
            .skeleton-content {{
                padding: 1.25rem;
            }}
            
            .skeleton-caption {{
                height: 16px;
                width: 80%;
            }}
            
            /* Modal */
            .modal-overlay {{
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.8);
                backdrop-filter: blur(10px);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 1000;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
            }}
            
            .modal-overlay.active {{
                opacity: 1;
                visibility: visible;
            }}
            
            .modal {{
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 20px;
                padding: 2rem;
                max-width: 400px;
                width: 90%;
                transform: scale(0.9);
                transition: transform 0.3s ease;
            }}
            
            .modal-overlay.active .modal {{
                transform: scale(1);
            }}
            
            .modal h3 {{
                font-size: 1.25rem;
                margin-bottom: 0.5rem;
            }}
            
            .modal p {{
                color: var(--text-secondary);
                margin-bottom: 1.5rem;
            }}
            
            .modal-actions {{
                display: flex;
                gap: 1rem;
            }}
            
            .modal-actions .btn {{
                flex: 1;
            }}
        </style>
    </head>
    <body>
        <header class="header">
            <div class="container">
                <div class="header-content">
                    <div class="logo">📸 PhotoFlow</div>
                    
                    <div class="header-actions">
                        <div class="user-menu">
                            <div class="user-avatar" id="user-avatar">?</div>
                            <span class="user-email" id="user-email">Yükleniyor...</span>
                        </div>
                        <button class="logout-btn" onclick="logout()" title="Çıkış Yap">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                                <polyline points="16 17 21 12 16 7"></polyline>
                                <line x1="21" y1="12" x2="9" y2="12"></line>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </header>
        
        <main class="container">
            <div class="main-content">
                <section class="feed-section">
                    <div class="feed-header">
                        <h2 class="feed-title">🔥 Keşfet</h2>
                        <button class="refresh-btn" onclick="loadFeed()" title="Yenile">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="23 4 23 10 17 10"></polyline>
                                <polyline points="1 20 1 14 7 14"></polyline>
                                <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
                            </svg>
                        </button>
                    </div>
                    
                    <div id="message-container"></div>
                    
                    <div class="feed-grid" id="feed-grid">
                        <!-- Posts will be loaded here -->
                    </div>
                </section>
                
                <aside class="sidebar">
                    <div class="upload-card">
                        <h3>
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                                <polyline points="17 8 12 3 7 8"></polyline>
                                <line x1="12" y1="3" x2="12" y2="15"></line>
                            </svg>
                            Yeni Paylaşım
                        </h3>
                        
                        <form id="upload-form">
                            <div class="upload-dropzone" id="dropzone">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                                    <circle cx="8.5" cy="8.5" r="1.5"></circle>
                                    <polyline points="21 15 16 10 5 21"></polyline>
                                </svg>
                                <p>Fotoğraf veya video yükle</p>
                                <p><span>Tıkla</span> veya sürükle bırak</p>
                                <input type="file" id="file-input" accept="image/*,video/*" hidden>
                            </div>
                            
                            <div class="upload-preview" id="upload-preview">
                                <img src="" alt="Preview" id="preview-img">
                                <video src="" id="preview-video" controls></video>
                                <button type="button" class="remove-btn" onclick="removeFile()">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                </button>
                            </div>
                            
                            <div class="upload-progress" id="upload-progress">
                                <div class="progress-bar">
                                    <div class="progress-fill" id="progress-fill"></div>
                                </div>
                                <p class="progress-text" id="progress-text">Yükleniyor...</p>
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">Açıklama</label>
                                <textarea name="caption" class="form-input" rows="3" placeholder="Bu fotoğraf/video hakkında bir şeyler yaz..."></textarea>
                            </div>
                            
                            <button type="submit" class="btn btn-primary btn-full" id="upload-btn" disabled>
                                <span class="btn-text">Paylaş</span>
                                <span class="spinner hidden"></span>
                            </button>
                        </form>
                    </div>
                </aside>
            </div>
        </main>
        
        <!-- Delete Confirmation Modal -->
        <div class="modal-overlay" id="delete-modal">
            <div class="modal">
                <h3>🗑️ Gönderiyi Sil</h3>
                <p>Bu gönderiyi silmek istediğinize emin misiniz? Bu işlem geri alınamaz.</p>
                <div class="modal-actions">
                    <button class="btn btn-secondary" onclick="closeDeleteModal()">İptal</button>
                    <button class="btn btn-danger" id="confirm-delete-btn">Sil</button>
                </div>
            </div>
        </div>
        
        <script>
            let currentUser = null;
            let selectedFile = null;
            let deletePostId = null;
            
            // Token'i al
            function getToken() {{
                var t = localStorage.getItem('access_token');
                if (!t || t === 'null' || t === 'undefined' || t === '') {{
                    return null;
                }}
                return t;
            }}
            
            // Auth check
            var token = getToken();
            console.log('Token kontrol:', token ? 'mevcut' : 'yok');
            
            // API helper
            async function api(endpoint, options) {{
                if (!options) options = {{}};
                var currentToken = getToken();
                console.log('API cagrisi:', endpoint);
                
                if (!currentToken) {{
                    console.log('Token yok, login sayfasina yonlendiriliyor');
                    window.location.href = '/';
                    return null;
                }}
                
                var headers = {{}};
                if (options.headers) {{
                    Object.assign(headers, options.headers);
                }}
                
                // FormData icin Content-Type ekleme
                if (!(options.body instanceof FormData)) {{
                    headers['Content-Type'] = 'application/json';
                }}
                headers['Authorization'] = 'Bearer ' + currentToken;
                
                var fetchOptions = {{
                    method: options.method || 'GET',
                    headers: headers
                }};
                if (options.body) {{
                    fetchOptions.body = options.body;
                }}
                
                try {{
                    var response = await fetch(endpoint, fetchOptions);
                    console.log('API yanit:', endpoint, response.status);
                    
                    if (response.status === 401) {{
                        console.log('401 hatasi - token gecersiz');
                        localStorage.removeItem('access_token');
                        window.location.href = '/';
                        return null;
                    }}
                    
                    return response;
                }} catch (error) {{
                    console.error('API Error:', error);
                    throw error;
                }}
            }}
            
            // Load current user
            async function loadUser() {{
                console.log('loadUser cagrildi');
                try {{
                    var response = await api('/users/me');
                    if (response && response.ok) {{
                        currentUser = await response.json();
                        document.getElementById('user-email').textContent = currentUser.email;
                        document.getElementById('user-avatar').textContent = currentUser.email[0].toUpperCase();
                        console.log('Kullanici yuklendi:', currentUser.email);
                    }} else {{
                        console.error('Kullanici yuklenemedi');
                    }}
                }} catch (error) {{
                    console.error('User load error:', error);
                }}
            }}
            
            // Show message
            function showMessage(message, type) {{
                if (!type) type = 'error';
                var container = document.getElementById('message-container');
                var icon = type === 'success' 
                    ? '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>'
                    : '<circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line>';
                container.innerHTML = '<div class="message message-' + type + ' animate-fade"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">' + icon + '</svg>' + message + '</div>';
                
                setTimeout(function() {{ container.innerHTML = ''; }}, 5000);
            }}
            
            // Load feed
            async function loadFeed() {{
                var feedGrid = document.getElementById('feed-grid');
                var refreshBtn = document.querySelector('.refresh-btn');
                
                refreshBtn.classList.add('loading');
                
                // Show skeletons
                feedGrid.innerHTML = '<div class="skeleton-post"><div class="skeleton-header"><div class="skeleton skeleton-avatar"></div><div class="skeleton skeleton-text"></div></div><div class="skeleton skeleton-media"></div></div>';
                
                try {{
                    var response = await api('/feed');
                    if (response && response.ok) {{
                        var data = await response.json();
                        console.log('Feed yuklendi:', data);
                        if (data.posts && Array.isArray(data.posts)) {{
                            renderPosts(data.posts);
                        }} else {{
                            console.error('Feed verisi beklenen formatta degil:', data);
                            renderPosts([]);
                        }}
                    }} else {{
                        console.error('Feed yuklenemedi:', response ? response.status : 'no response');
                        renderPosts([]);
                    }}
                }} catch (error) {{
                    console.error('Feed error:', error);
                    feedGrid.innerHTML = '<div class="empty-state"><h3>Bir hata olustu</h3><p>Feed yuklenirken bir sorun olustu.</p></div>';
                }} finally {{
                    refreshBtn.classList.remove('loading');
                }}
            }}
            
            // Render posts
            function renderPosts(posts) {{
                var feedGrid = document.getElementById('feed-grid');
                
                if (posts.length === 0) {{
                    feedGrid.innerHTML = '<div class="empty-state"><h3>Henuz gonderi yok</h3><p>Ilk gonderiyi sen paylas!</p></div>';
                    return;
                }}
                
                var html = '';
                for (var i = 0; i < posts.length; i++) {{
                    var post = posts[i];
                    var avatar = post.email ? post.email[0].toUpperCase() : '?';
                    var username = post.email ? post.email.split('@')[0] : 'Anonim';
                    var dateStr = formatDate(post.created_at);
                    var ownerBadge = post.is_owner ? '<span class="owner-badge">Sen</span>' : '';
                    
                    var media = '';
                    if (post.file_type === 'video') {{
                        media = '<video src="' + post.url + '" controls preload="metadata"></video>';
                    }} else {{
                        media = '<img src="' + post.url + '" alt="Post" loading="lazy">';
                    }}
                    
                    var caption = '';
                    if (post.caption) {{
                        caption = '<div class="post-content"><p class="post-caption">' + post.caption + '</p></div>';
                    }}
                    
                    var menuHtml = '';
                    if (post.is_owner) {{
                        menuHtml = '<div class="post-menu"><button class="post-menu-btn" onclick="toggleDropdown(this)"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="1"></circle><circle cx="12" cy="5" r="1"></circle><circle cx="12" cy="19" r="1"></circle></svg></button><div class="post-dropdown"><button class="dropdown-item danger" data-postid="' + post.id + '" onclick="openDeleteModal(this.dataset.postid)">Sil</button></div></div>';
                    }}
                    
                    html += '<article class="post-card">';
                    html += '<div class="post-header">';
                    html += '<div class="post-author">';
                    html += '<div class="post-avatar">' + avatar + '</div>';
                    html += '<div class="post-author-info"><h4>' + username + '</h4><span>' + dateStr + '</span></div>';
                    html += ownerBadge;
                    html += '</div>';
                    html += menuHtml;
                    html += '</div>';
                    html += '<div class="post-media">' + media + '</div>';
                    html += caption;
                    html += '</article>';
                }}
                
                feedGrid.innerHTML = html;
            }}
            
            // Format date
            function formatDate(dateString) {{
                var date = new Date(dateString);
                var now = new Date();
                var diff = now - date;
                
                var minutes = Math.floor(diff / 60000);
                var hours = Math.floor(diff / 3600000);
                var days = Math.floor(diff / 86400000);
                
                if (minutes < 1) return 'Simdi';
                if (minutes < 60) return minutes + ' dk once';
                if (hours < 24) return hours + ' saat once';
                if (days < 7) return days + ' gun once';
                
                return date.toLocaleDateString('tr-TR');
            }}
            
            // Dropdown toggle
            function toggleDropdown(btn) {{
                var dropdown = btn.nextElementSibling;
                var allDropdowns = document.querySelectorAll('.post-dropdown.active');
                for (var i = 0; i < allDropdowns.length; i++) {{
                    if (allDropdowns[i] !== dropdown) allDropdowns[i].classList.remove('active');
                }}
                dropdown.classList.toggle('active');
            }}
            
            // Close dropdowns on outside click
            document.addEventListener('click', function(e) {{
                if (!e.target.closest('.post-menu')) {{
                    var dropdowns = document.querySelectorAll('.post-dropdown.active');
                    for (var i = 0; i < dropdowns.length; i++) {{
                        dropdowns[i].classList.remove('active');
                    }}
                }}
            }});
            
            // Delete modal
            function openDeleteModal(postId) {{
                deletePostId = postId;
                document.getElementById('delete-modal').classList.add('active');
            }}
            
            function closeDeleteModal() {{
                deletePostId = null;
                document.getElementById('delete-modal').classList.remove('active');
            }}
            
            document.getElementById('confirm-delete-btn').addEventListener('click', async function() {{
                if (!deletePostId) return;
                
                var btn = document.getElementById('confirm-delete-btn');
                btn.disabled = true;
                btn.textContent = 'Siliniyor...';
                
                try {{
                    var response = await api('/posts/' + deletePostId, {{ method: 'DELETE' }});
                    if (response && response.ok) {{
                        showMessage('Gonderi basariyla silindi!', 'success');
                        loadFeed();
                    }} else if (response) {{
                        var error = await response.json();
                        showMessage(error.detail || 'Silme islemi basarisiz.');
                    }}
                }} catch (error) {{
                    showMessage('Bir hata olustu.');
                }} finally {{
                    btn.disabled = false;
                    btn.textContent = 'Sil';
                    closeDeleteModal();
                }}
            }});
            
            // File upload
            var dropzone = document.getElementById('dropzone');
            var fileInput = document.getElementById('file-input');
            var uploadPreview = document.getElementById('upload-preview');
            var previewImg = document.getElementById('preview-img');
            var previewVideo = document.getElementById('preview-video');
            var uploadBtn = document.getElementById('upload-btn');
            
            dropzone.addEventListener('click', function() {{ fileInput.click(); }});
            
            dropzone.addEventListener('dragover', function(e) {{
                e.preventDefault();
                dropzone.classList.add('dragover');
            }});
            
            dropzone.addEventListener('dragleave', function() {{
                dropzone.classList.remove('dragover');
            }});
            
            dropzone.addEventListener('drop', function(e) {{
                e.preventDefault();
                dropzone.classList.remove('dragover');
                var file = e.dataTransfer.files[0];
                if (file) handleFile(file);
            }});
            
            fileInput.addEventListener('change', function(e) {{
                var file = e.target.files[0];
                if (file) handleFile(file);
            }});
            
            function handleFile(file) {{
                if (!file.type.startsWith('image/') && !file.type.startsWith('video/')) {{
                    showMessage('Sadece fotograf ve video yukleyebilirsiniz.');
                    return;
                }}
                
                if (file.size > 50 * 1024 * 1024) {{
                    showMessage('Dosya boyutu 50MB dan kucuk olmalidir.');
                    return;
                }}
                
                selectedFile = file;
                uploadBtn.disabled = false;
                
                var url = URL.createObjectURL(file);
                
                if (file.type.startsWith('video/')) {{
                    previewImg.style.display = 'none';
                    previewVideo.style.display = 'block';
                    previewVideo.src = url;
                }} else {{
                    previewVideo.style.display = 'none';
                    previewImg.style.display = 'block';
                    previewImg.src = url;
                }}
                
                dropzone.style.display = 'none';
                uploadPreview.classList.add('active');
            }}
            
            function removeFile() {{
                selectedFile = null;
                uploadBtn.disabled = true;
                fileInput.value = '';
                
                previewImg.src = '';
                previewVideo.src = '';
                
                dropzone.style.display = 'block';
                uploadPreview.classList.remove('active');
            }}
            
            // Upload form
            document.getElementById('upload-form').addEventListener('submit', async function(e) {{
                e.preventDefault();
                
                if (!selectedFile) return;
                
                var btn = document.getElementById('upload-btn');
                var btnText = btn.querySelector('.btn-text');
                var spinner = btn.querySelector('.spinner');
                var progressContainer = document.getElementById('upload-progress');
                var progressFill = document.getElementById('progress-fill');
                var progressText = document.getElementById('progress-text');
                
                btn.disabled = true;
                btnText.textContent = 'Yukleniyor...';
                spinner.classList.remove('hidden');
                progressContainer.classList.add('active');
                
                var formData = new FormData();
                formData.append('file', selectedFile);
                formData.append('caption', e.target.caption.value);
                
                // Simulated progress
                var progress = 0;
                var progressInterval = setInterval(function() {{
                    progress += Math.random() * 15;
                    if (progress > 90) progress = 90;
                    progressFill.style.width = progress + '%';
                    progressText.textContent = 'Yukleniyor... ' + Math.round(progress) + '%';
                }}, 200);
                
                try {{
                    console.log('Dosya yukleniyor:', selectedFile.name);
                    var response = await api('/upload', {{
                        method: 'POST',
                        body: formData
                    }});
                    
                    clearInterval(progressInterval);
                    progressFill.style.width = '100%';
                    progressText.textContent = 'Tamamlandi!';
                    
                    if (response && response.ok) {{
                        var result = await response.json();
                        console.log('Yukleme basarili:', result);
                        showMessage('Gonderiniz basariyla paylasildi!', 'success');
                        removeFile();
                        e.target.caption.value = '';
                        loadFeed();
                    }} else if (response) {{
                        var errorData = await response.json();
                        console.error('Yukleme hatasi:', errorData);
                        showMessage(errorData.detail || 'Yukleme basarisiz.');
                    }} else {{
                        showMessage('Baglanti hatasi. Lutfen giris yapin.');
                    }}
                }} catch (error) {{
                    console.error('Upload error:', error);
                    clearInterval(progressInterval);
                    showMessage('Yukleme sirasinda bir hata olustu: ' + error.message);
                }} finally {{
                    btn.disabled = !selectedFile;
                    btnText.textContent = 'Paylas';
                    spinner.classList.add('hidden');
                    
                    setTimeout(function() {{
                        progressContainer.classList.remove('active');
                        progressFill.style.width = '0%';
                    }}, 1000);
                }}
            }});
            
            // Logout
            function logout() {{
                console.log('Cikis yapiliyor...');
                localStorage.removeItem('access_token');
                localStorage.clear();
                window.location.href = '/';
            }}
            
            // Global scope'a fonksiyonları aç (onclick için gerekli)
            window.logout = logout;
            window.loadFeed = loadFeed;
            window.loadUser = loadUser;
            window.toggleDropdown = toggleDropdown;
            window.openDeleteModal = openDeleteModal;
            window.closeDeleteModal = closeDeleteModal;
            window.removeFile = removeFile;
            
            // Init - sayfa yüklendiğinde çalış
            console.log('=== SAYFA BASLATILIYOR ===');
            console.log('Token durumu:', token ? 'mevcut' : 'yok');
            
            if (token) {{
                console.log('Token bulundu, veriler yukleniyor...');
                loadUser();
                loadFeed();
            }} else {{
                console.log('Token bulunamadi, login sayfasina yonlendiriliyor');
                window.location.href = '/';
            }}
        </script>
    </body>
    </html>
    """


@router.get("/", response_class=HTMLResponse)
async def auth_page():
    """Ana sayfa - Giriş/Kayıt ekranı"""
    return get_auth_page()


@router.get("/app", response_class=HTMLResponse)
async def app_page():
    """Uygulama ana sayfası - Feed ve upload"""
    return get_app_page()

