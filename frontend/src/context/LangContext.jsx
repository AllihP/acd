import { createContext, useContext, useState, useEffect } from 'react'

const LangContext = createContext()

// Traductions UI (labels fixes, pas venant du backend)
export const UI_STRINGS = {
  fr: {
    nav_home:         'Accueil',
    nav_about:        'À propos',
    nav_realisations: 'Réalisations',
    nav_projets:      'Projets',
    nav_contact:      'Contact',
    loading:          'Chargement…',
    error:            'Impossible de charger les données.',
    all:              'Tout',
    featured:         'Mis en avant',
    view_all:         'Voir tout',
    send:             'Envoyer ma demande →',
    sending:          'Envoi en cours…',
    sent:             '✓ Message envoyé !',
    form_name:        'Nom complet *',
    form_company:     'Entreprise / Organisation',
    form_phone:       'Téléphone *',
    form_email:       'Email *',
    form_service:     'Service souhaité',
    form_select:      '— Sélectionnez —',
    form_message:     'Votre message *',
    form_err_name:    'Veuillez saisir votre nom.',
    form_err_email:   'Email invalide.',
    form_err_phone:   'Téléphone requis.',
    form_err_message: 'Message requis.',
    why_eyebrow:      '— Pourquoi nous choisir',
    testi_eyebrow:    '— Témoignages',
    testi_title:      'Ils nous ont fait confiance',
    svc_eyebrow:      '— Nos expertises',
    pf_eyebrow:       '— Nos réalisations',
    footer_nav:       'Navigation',
    footer_services:  'Services',
    footer_contact:   'Contact',
    footer_desc:      "Agence de Communication pour le Développement. Nous donnons vie à vos idées et propulsons votre marque vers l'excellence.",
    addr_label:       'Adresse',
    phone_label:      'Téléphone',
    copy:             '© 2025 ACD — Tous droits réservés.',
    cat_all:          'Tout',
    cat_branding:     'Branding',
    cat_digital:      'Digital',
    cat_evenement:    'Événement',
    cat_print:        'Print',
    cat_social:       'Social Media',
    cat_audiovisuel:  'Audiovisuel',
    years_exp:        "ans d'expertise",
    service_options: [
      { value: 'branding',    label: 'Branding & Identité' },
      { value: 'digital',     label: 'Marketing Digital' },
      { value: 'evenement',   label: 'Événementiel' },
      { value: 'print',       label: 'Print & Édition' },
      { value: 'social',      label: 'Social Media' },
      { value: 'audiovisuel', label: 'Audiovisuel' },
      { value: 'conseil',     label: 'Conseil Stratégique' },
      { value: 'autre',       label: 'Autre' },
    ],
  },
  en: {
    nav_home:         'Home',
    nav_about:        'About',
    nav_realisations: 'Portfolio',
    nav_projets:      'Services',
    nav_contact:      'Contact',
    loading:          'Loading…',
    error:            'Failed to load data.',
    all:              'All',
    featured:         'Featured',
    view_all:         'View all',
    send:             'Send My Request →',
    sending:          'Sending…',
    sent:             '✓ Message Sent!',
    form_name:        'Full Name *',
    form_company:     'Company / Organization',
    form_phone:       'Phone *',
    form_email:       'Email *',
    form_service:     'Service Needed',
    form_select:      '— Select —',
    form_message:     'Your Message *',
    form_err_name:    'Please enter your name.',
    form_err_email:   'Invalid email.',
    form_err_phone:   'Phone required.',
    form_err_message: 'Message required.',
    why_eyebrow:      '— Why Choose Us',
    testi_eyebrow:    '— Testimonials',
    testi_title:      'They Trusted Us',
    svc_eyebrow:      '— Our Expertise',
    pf_eyebrow:       '— Our Portfolio',
    footer_nav:       'Navigation',
    footer_services:  'Services',
    footer_contact:   'Contact',
    footer_desc:      'Agency for Communication and Development. We bring your ideas to life and propel your brand to excellence.',
    addr_label:       'Address',
    phone_label:      'Phone',
    copy:             '© 2025 ACD — All rights reserved.',
    cat_all:          'All',
    cat_branding:     'Branding',
    cat_digital:      'Digital',
    cat_evenement:    'Events',
    cat_print:        'Print',
    cat_social:       'Social Media',
    cat_audiovisuel:  'Audiovisual',
    years_exp:        'years of expertise',
    service_options: [
      { value: 'branding',    label: 'Branding & Identity' },
      { value: 'digital',     label: 'Digital Marketing' },
      { value: 'evenement',   label: 'Events' },
      { value: 'print',       label: 'Print & Publishing' },
      { value: 'social',      label: 'Social Media' },
      { value: 'audiovisuel', label: 'Audiovisual' },
      { value: 'conseil',     label: 'Strategic Advisory' },
      { value: 'autre',       label: 'Other' },
    ],
  },
  ar: {
    dir:              'rtl',
    nav_home:         'الرئيسية',
    nav_about:        'من نحن',
    nav_realisations: 'أعمالنا',
    nav_projets:      'خدماتنا',
    nav_contact:      'اتصل بنا',
    loading:          '…جارٍ التحميل',
    error:            'تعذر تحميل البيانات.',
    all:              'الكل',
    featured:         'مميز',
    view_all:         'عرض الكل',
    send:             'إرسال طلبي ←',
    sending:          '…جارٍ الإرسال',
    sent:             '✓ تم إرسال الرسالة!',
    form_name:        'الاسم الكامل *',
    form_company:     'الشركة / المؤسسة',
    form_phone:       'الهاتف *',
    form_email:       'البريد الإلكتروني *',
    form_service:     'الخدمة المطلوبة',
    form_select:      '— اختر —',
    form_message:     'رسالتك *',
    form_err_name:    'الرجاء إدخال اسمك.',
    form_err_email:   'البريد الإلكتروني غير صالح.',
    form_err_phone:   'الهاتف مطلوب.',
    form_err_message: 'الرسالة مطلوبة.',
    why_eyebrow:      '— لماذا تختارنا',
    testi_eyebrow:    '— شهادات عملائنا',
    testi_title:      'وثقوا بنا',
    svc_eyebrow:      '— خبراتنا',
    pf_eyebrow:       '— أعمالنا',
    footer_nav:       'التنقل',
    footer_services:  'الخدمات',
    footer_contact:   'التواصل',
    footer_desc:      'وكالة الاتصال من أجل التنمية. نحوّل أفكارك إلى واقع ونرفع علامتك إلى القمة.',
    addr_label:       'العنوان',
    phone_label:      'الهاتف',
    copy:             '.© 2025 ACD — جميع الحقوق محفوظة',
    cat_all:          'الكل',
    cat_branding:     'الهوية البصرية',
    cat_digital:      'الرقمي',
    cat_evenement:    'الفعاليات',
    cat_print:        'المطبوعات',
    cat_social:       'السوشال ميديا',
    cat_audiovisuel:  'الإنتاج المرئي',
    years_exp:        'سنوات من الخبرة',
    service_options: [
      { value: 'branding',    label: 'الهوية البصرية' },
      { value: 'digital',     label: 'التسويق الرقمي' },
      { value: 'evenement',   label: 'إدارة الفعاليات' },
      { value: 'print',       label: 'المطبوعات' },
      { value: 'social',      label: 'السوشال ميديا' },
      { value: 'audiovisuel', label: 'الإنتاج المرئي والسمعي' },
      { value: 'conseil',     label: 'الاستشارات الاستراتيجية' },
      { value: 'autre',       label: 'أخرى' },
    ],
  }
}

// Helper : récupère le bon champ traduit depuis un objet backend
export function t(obj, lang, field) {
  if (!obj) return ''
  return obj[`${field}_${lang}`] || obj[`${field}_fr`] || obj[`${field}_en`] || ''
}

export function LangProvider({ children }) {
  const [lang, setLang] = useState(() => localStorage.getItem('acd_lang') || 'fr')

  useEffect(() => {
    const dir = UI_STRINGS[lang]?.dir || 'ltr'
    document.documentElement.lang = lang
    document.documentElement.dir  = dir
    localStorage.setItem('acd_lang', lang)
  }, [lang])

  const ui = UI_STRINGS[lang] || UI_STRINGS.fr
  return (
    <LangContext.Provider value={{ lang, setLang, ui }}>
      {children}
    </LangContext.Provider>
  )
}

export function useLang() {
  return useContext(LangContext)
}
