import string
import os

reg_id_sl = {
  'EU' : 1,
  'CIS' : 2,
  'NA' : 3,
  'AS' : 4,
  'SA' : 5,
  'OC' : 6,
  'AF' : 7,
  'Other' : 8
}

sok_country_sl = {'AD': 'Andorra', 'AE': 'United Arab Emirates', 'AF': 'Afghanistan', 'AG': 'Antigua & Barbuda', 'AI': 'Anguilla', 'AL': 'Albania', 'AM': 'Armenia', 'AN': 'Netherlands Antilles', 'AO': 'Angola', 'AQ': 'Antarctica', 'AR': 'Argentina', 'AS': 'American Samoa', 'AT': 'Austria', 'AU': 'Australia', 'AW': 'Aruba', 'AX': 'Aland Islands', 'AZ': 'Azerbaijan', 'BA': 'Bosnia and Herzegovina', 'BB': 'Barbados', 'BD': 'Bangladesh', 'BE': 'Belgium', 'BF': 'Burkina Faso', 'BG': 'Bulgaria', 'BH': 'Bahrain', 'BI': 'Burundi', 'BJ': 'Benin', 'BM': 'Bermuda', 'BN': 'Brunei Darussalam', 'BO': 'Bolivia', 'BR': 'Brazil', 'BS': 'Bahama', 'BT': 'Bhutan', 'BU': 'Burma (no longer exists)', 'BV': 'Bouvet Island', 'BW': 'Botswana', 'BY': 'Belarus', 'BZ': 'Belize', 'CA': 'Canada', 'CC': 'Cocos (Keeling) Islands', 'CF': 'Central African Republic', 'CG': 'Congo', 'CH': 'Switzerland', 'CI': "Cote D''ivoire (Ivory Coast)", 'CK': 'Cook Iislands', 'CL': 'Chile', 'CM': 'Cameroon', 'CN': 'China', 'CO': 'Colombia', 'CR': 'Costa Rica', 'CS': 'Czechoslovakia (no longer exists)', 'CU': 'Cuba', 'CV': 'Cape Verde', 'CW': 'Curacao', 'CX': 'Christmas Island', 'CY': 'Cyprus', 'CZ': 'Czech Republic', 'DD': 'German Democratic Republic (no longer exists)', 'DE': 'Germany', 'DJ': 'Djibouti', 'DK': 'Denmark', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'DZ': 'Algeria', 'EC': 'Ecuador', 'EE': 'Estonia', 'EG': 'Egypt', 'EH': 'Western Sahara', 'ER': 'Eritrea', 'ES': 'Spain', 'ET': 'Ethiopia', 'FI': 'Finland', 'FJ': 'Fiji', 'FK': 'Falkland Islands (Malvinas)', 'FM': 'Micronesia', 'FO': 'Faroe Islands', 'FR': 'France', 'FX': 'France, Metropolitan', 'GA': 'Gabon', 'GB': 'United Kingdom (Great Britain)', 'GD': 'Grenada', 'GE': 'Georgia', 'GF': 'French Guiana', 'GG': 'Guernsey', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GL': 'Greenland', 'GM': 'Gambia', 'GN': 'Guinea', 'GP': 'Guadeloupe', 'GQ': 'Equatorial Guinea', 'GR': 'Greece', 'GS': 'South Georgia and the South Sandwich Islands', 'GT': 'Guatemala', 'GU': 'Guam', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HK': 'Hong Kong', 'HM': 'Heard & McDonald Islands', 'HN': 'Honduras', 'HR': 'Croatia', 'HT': 'Haiti', 'HU': 'Hungary', 'ID': 'Indonesia', 'IE': 'Ireland', 'IL': 'Israel', 'IM': 'Isle of Men', 'IN': 'India', 'IO': 'British Indian Ocean Territory', 'IQ': 'Iraq', 'IR': 'Islamic Republic of Iran', 'IS': 'Iceland', 'IT': 'Italy', 'JE': 'Jersey', 'JM': 'Jamaica', 'JO': 'Jordan', 'JP': 'Japan', 'KE': 'Kenya', 'KG': 'Kyrgyzstan', 'KH': 'Cambodia', 'KI': 'Kiribati', 'KM': 'Comoros', 'KN': 'St. Kitts and Nevis', 'KR': 'Korea, Republic of', 'KW': 'Kuwait', 'KY': 'Cayman Islands', 'KZ': 'Kazakhstan', 'LA': "Lao People's Democratic Republic", 'LB': 'Lebanon', 'LC': 'Saint Lucia', 'LI': 'Liechtenstein', 'LK': 'Sri Lanka', 'LR': 'Liberia', 'LS': 'Lesotho', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'LV': 'Latvia', 'LY': 'Libyan Arab Jamahiriya', 'MA': 'Morocco', 'MC': 'Monaco', 'MD': 'Moldova, Republic of', 'ME': 'Montenegro', 'MG': 'Madagascar', 'MH': 'Marshall Islands', 'MK': 'Macedonia', 'ML': 'Mali', 'MM': 'Myanmar', 'MN': 'Mongolia', 'MO': 'Macau', 'MP': 'Northern Mariana Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MS': 'Monserrat', 'MT': 'Malta', 'MU': 'Mauritius', 'MV': 'Maldives', 'MW': 'Malawi', 'MX': 'Mexico', 'MY': 'Malaysia', 'MZ': 'Mozambique', 'NA': 'Nambia', 'NC': 'New Caledonia', 'NE': 'Niger', 'NF': 'Norfolk Island', 'NG': 'Nigeria', 'NI': 'Nicaragua', 'NL': 'Netherlands', 'NO': 'Norway', 'NP': 'Nepal', 'NR': 'Nauru', 'NT': 'Neutral Zone (no longer exists)', 'NU': 'Niue', 'NZ': 'New Zealand', 'OM': 'Oman', 'PA': 'Panama', 'PE': 'Peru', 'PF': 'French Polynesia', 'PG': 'Papua New Guinea', 'PH': 'Philippines', 'PK': 'Pakistan', 'PL': 'Poland', 'PM': 'St. Pierre & Miquelon', 'PN': 'Pitcairn', 'PR': 'Puerto Rico', 'PS': 'Palestine', 'PT': 'Portugal', 'PW': 'Palau', 'PY': 'Paraguay', 'QA': 'Qatar', 'RE': 'Reunion', 'RO': 'Romania', 'RS': 'Serbia', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'SA': 'Saudi Arabia', 'SB': 'Solomon Islands', 'SC': 'Seychelles', 'SD': 'Sudan', 'SE': 'Sweden', 'SG': 'Singapore', 'SH': 'St Helena', 'SI': 'Slovenia', 'SJ': 'Svalbard & Jan Mayen Islands', 'SK': 'Slovakia', 'SL': 'Sierra Leone', 'SM': 'San Marino', 'SN': 'Senegal', 'SO': 'Somalia', 'SR': 'Suriname', 'ST': 'Sao Tome & Principe', 'SU': 'Union of Soviet Socialist Republics (no longer exi', 'SV': 'El Salvador', 'SY': 'Syrian Arab Republic', 'SZ': 'Swaziland', 'TC': 'Turks & Caicos Islands', 'TD': 'Chad', 'TF': 'French Southern Territories', 'TG': 'Togo', 'TH': 'Thailand', 'TJ': 'Tajikistan', 'TK': 'Tokelau', 'TM': 'Turkmenistan', 'TN': 'Tunisia', 'TO': 'Tonga', 'TP': 'East Timor', 'TR': 'Turkey', 'TT': 'Trinidad & Tobago', 'TV': 'Tuvalu', 'TW': 'Taiwan, Province of China', 'TZ': 'Tanzania, United Republic of', 'UA': 'Ukraine', 'UG': 'Uganda', 'UM': 'United States Minor Outlying Islands', 'US': 'United States of America', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VA': 'Vatican City State (Holy See)', 'VC': 'St. Vincent & the Grenadines', 'VE': 'Venezuela', 'VG': 'British Virgin Islands', 'VI': 'United States Virgin Islands', 'VN': 'Viet Nam', 'VU': 'Vanuatu', 'WF': 'Wallis & Futuna Islands', 'WS': 'Samoa', 'XK': 'Kosovo', 'YD': 'Democratic Yemen (no longer exists)', 'YE': 'Yemen', 'YT': 'Mayotte', 'YU': 'Yugoslavia', 'ZA': 'South Africa', 'ZM': 'Zambia', 'ZR': 'Zaire', 'ZW': 'Zimbabwe'}

country_reg_sl = {'DE': 'EU', 'PL': 'EU', 'GB': 'EU', 'ES': 'EU', 'SE': 'EU', 'LV': 'EU', 'FR': 'EU', 'RS': 'EU', 'HR': 'EU', 'EE': 'EU', 'BE': 'EU', 'IT': 'EU', 'SK': 'EU', 'AT': 'EU', 'LT': 'EU', 'FI': 'EU', 'NL': 'EU', 'RO': 'EU', 'CZ': 'EU', 'CH': 'EU', 'LU': 'EU', 'PT': 'EU', 'DK': 'EU', 'HU': 'EU', 'GR': 'EU', 'NO': 'EU', 'BG': 'EU', 'JE': 'EU', 'IS': 'EU', 'IE': 'EU', 'CY': 'EU', 'MT': 'EU', 'ME': 'EU', 'SI': 'EU', 'BA': 'EU', 'KG': 'AS', 'IN': 'AS', 'TR': 'AS', 'PH': 'AS', 'KR': 'AS', 'IL': 'AS', 'AE': 'AS', 'SG': 'AS', 'TH': 'AS', 'IQ': 'AS', 'SA': 'AS', 'VN': 'AS', 'MN': 'AS', 'ID': 'AS', 'TW': 'AS', 'IR': 'AS', 'JP': 'AS', 'MY': 'AS', 'KW': 'AS', 'HK': 'AS', 'CN': 'AS', 'BH': 'AS', 'BD': 'AS', 'LK': 'AS', 'QA': 'AS', 'LA': 'AS', 'BN': 'AS', 'NP': 'AS', 'CL': 'SA', 'BR': 'SA', 'AR': 'SA', 'CO': 'SA', 'PE': 'SA', 'UY': 'SA', 'PY': 'SA', 'EC': 'SA', 'SR': 'SA', 'ZA': 'AF', 'DZ': 'AF', 'TN': 'AF', 'RE': 'AF', 'EG': 'AF', 'CG': 'AF', 'MA': 'AF', 'DJ': 'AF', 'BF': 'AF', 'CM': 'AF', 'MG': 'AF', 'NG': 'AF', 'GA': 'AF', 'SN': 'AF', 'AU': 'OC', 'PF': 'OC', 'NZ': 'OC', 'US': 'NA', 'CR': 'NA', 'CA': 'NA', 'MX': 'NA', 'VC': 'NA', 'PA': 'NA', 'SV': 'NA', 'PR': 'NA', 'DO': 'NA', 'CW': 'NA', 'AW': 'NA', 'UA': 'CIS', 'RU': 'CIS', 'BY': 'CIS', 'KZ': 'CIS', 'UZ': 'CIS', 'KJ': 'CIS', 'MD': 'CIS', 'AZ': 'CIS', 'AM': 'CIS', 'TJ': 'CIS', 'GE': 'CIS', 'NC': 'OC', 'VE': 'SA', 'GU': 'OC', 'ML': 'AF', 'XK': 'EU', 'GI': 'EU', 'AL': 'EU', 'PK': 'AS', 'CU': 'NA', 'GG': 'EU', 'ZM': 'AF', 'PS': 'AS', 'TT': 'SA', 'BO': 'SA', 'OM': 'AS', 'JM': 'NA', 'MK': 'EU', 'KE': 'AF', 'NI': 'NA', 'LB': 'AS', 'IM': 'EU', 'MM': 'AS', 'BB': 'NA', 'JO': 'AS', 'YE': 'AS', 'HN': 'NA', 'GT': 'NA', 'BT': 'AS', 'BM': 'NA', 'FO': 'EU', 'AS': 'OC', 'GP': 'NA', 'GF': 'SA', 'TM': 'AS', 'AD': 'EU', 'CI': 'AF', 'BS': 'NA', 'GH': 'AF', 'MC': 'EU', 'LY': 'AF', 'MQ': 'SA', 'MV': 'AS', 'VI': 'SA', 'AF': 'AS', 'AX': 'EU'}

region_full_sl = {
    'EU' : 'Europe',
    'CIS' : 'Commonwealth of Independent States',
    'NA' : 'North America',
    'AS' : 'Asia',
    'SA' : 'South America',
    'OC' : 'Oceania',
    'AF' : 'Africa',
    'Other' : 'Other'
}


def reg_id(region_name):#перевод региона в номер
    if region_name in reg_id_sl:
        res = reg_id_sl[region_name]
    else:
        res = 'ERROR1 region to number'
    return str(res)

def sok_country(country_code):#перевод сокращения в страну
    if country_code in sok_country_sl:
        res = sok_country_sl[country_code]
    else:
        res = 'ERROR2 abbreviation to country'
    return str(res)

def country_reg(country_code):#перевод страны в регион
    if country_code in country_reg_sl:
        res = country_reg_sl[country_code]
    else:
        res = 'ERROR3 country to short region'
    return str(res)

def region_full(region_short):#перевод региона в номер
    if region_short in region_full_sl:
        res = region_full_sl[region_short]
    else:
        res = 'ERROR4 short region to full region'
    return str(res)


count = 0
with open("countries.txt", "r") as countries:
    with open("result.txt", "w+") as result:
        result.write("INSERT INTO marketing_events.country_region \n(country_code, region_id, region_name, country_name) VALUES \n")
        lines = countries.read().splitlines()
        for line in lines:
            result.write("(\'"+line+"', "+ reg_id(country_reg(line))+", '"+ region_full(country_reg(line))+"', '"+ sok_country(line)+"'),\n")
    with open("result.txt", 'rb+') as result: # удаление последней
        result.seek(-2, os.SEEK_END)
        result.truncate()
