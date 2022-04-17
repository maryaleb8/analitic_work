import string
import os

reg_id_sl = {
  'EU' : 1,
  'AS' : 2,
  'SA' : 3,
  'AF' : 4,
  'OC' : 5,
  'CIS' : 6,
  'NA' : 7,
  'Other' : 8
}

sok_country_sl = {'AD': 'Andorra', 'AE': 'United Arab Emirates', 'AF': 'Afghanistan', 'AG': 'Antigua & Barbuda', 'AI': 'Anguilla', 'AL': 'Albania', 'AM': 'Armenia', 'AN': 'Netherlands Antilles', 'AO': 'Angola', 'AQ': 'Antarctica', 'AR': 'Argentina', 'AS': 'American Samoa', 'AT': 'Austria', 'AU': 'Australia', 'AW': 'Aruba', 'AX': 'Aland Islands', 'AZ': 'Azerbaijan', 'BA': 'Bosnia and Herzegovina', 'BB': 'Barbados', 'BD': 'Bangladesh', 'BE': 'Belgium', 'BF': 'Burkina Faso', 'BG': 'Bulgaria', 'BH': 'Bahrain', 'BI': 'Burundi', 'BJ': 'Benin', 'BM': 'Bermuda', 'BN': 'Brunei Darussalam', 'BO': 'Bolivia', 'BR': 'Brazil', 'BS': 'Bahama', 'BT': 'Bhutan', 'BU': 'Burma (no longer exists)', 'BV': 'Bouvet Island', 'BW': 'Botswana', 'BY': 'Belarus', 'BZ': 'Belize', 'CA': 'Canada', 'CC': 'Cocos (Keeling) Islands', 'CF': 'Central African Republic', 'CG': 'Congo', 'CH': 'Switzerland', 'CI': "CГґte D'ivoire (Ivory Coast)", 'CK': 'Cook Iislands', 'CL': 'Chile', 'CM': 'Cameroon', 'CN': 'China', 'CO': 'Colombia', 'CR': 'Costa Rica', 'CS': 'Czechoslovakia (no longer exists)', 'CU': 'Cuba', 'CV': 'Cape Verde', 'CW': 'Curacao', 'CX': 'Christmas Island', 'CY': 'Cyprus', 'CZ': 'Czech Republic', 'DD': 'German Democratic Republic (no longer exists)', 'DE': 'Germany', 'DJ': 'Djibouti', 'DK': 'Denmark', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'DZ': 'Algeria', 'EC': 'Ecuador', 'EE': 'Estonia', 'EG': 'Egypt', 'EH': 'Western Sahara', 'ER': 'Eritrea', 'ES': 'Spain', 'ET': 'Ethiopia', 'FI': 'Finland', 'FJ': 'Fiji', 'FK': 'Falkland Islands (Malvinas)', 'FM': 'Micronesia', 'FO': 'Faroe Islands', 'FR': 'France', 'FX': 'France, Metropolitan', 'GA': 'Gabon', 'GB': 'United Kingdom (Great Britain)', 'GD': 'Grenada', 'GE': 'Georgia', 'GF': 'French Guiana', 'GG': 'Guernsey', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GL': 'Greenland', 'GM': 'Gambia', 'GN': 'Guinea', 'GP': 'Guadeloupe', 'GQ': 'Equatorial Guinea', 'GR': 'Greece', 'GS': 'South Georgia and the South Sandwich Islands', 'GT': 'Guatemala', 'GU': 'Guam', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HK': 'Hong Kong', 'HM': 'Heard & McDonald Islands', 'HN': 'Honduras', 'HR': 'Croatia', 'HT': 'Haiti', 'HU': 'Hungary', 'ID': 'Indonesia', 'IE': 'Ireland', 'IL': 'Israel', 'IM': 'Isle of Men', 'IN': 'India', 'IO': 'British Indian Ocean Territory', 'IQ': 'Iraq', 'IR': 'Islamic Republic of Iran', 'IS': 'Iceland', 'IT': 'Italy', 'JE': 'Jersey', 'JM': 'Jamaica', 'JO': 'Jordan', 'JP': 'Japan', 'KE': 'Kenya', 'KG': 'Kyrgyzstan', 'KH': 'Cambodia', 'KI': 'Kiribati', 'KM': 'Comoros', 'KN': 'St. Kitts and Nevis', 'KP': "Korea, Democratic People's Republic of", 'KR': 'Korea, Republic of', 'KW': 'Kuwait', 'KY': 'Cayman Islands', 'KZ': 'Kazakhstan', 'LA': "Lao People's Democratic Republic", 'LB': 'Lebanon', 'LC': 'Saint Lucia', 'LI': 'Liechtenstein', 'LK': 'Sri Lanka', 'LR': 'Liberia', 'LS': 'Lesotho', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'LV': 'Latvia', 'LY': 'Libyan Arab Jamahiriya', 'MA': 'Morocco', 'MC': 'Monaco', 'MD': 'Moldova, Republic of', 'ME': 'Montenegro', 'MG': 'Madagascar', 'MH': 'Marshall Islands', 'MK': 'Macedonia', 'ML': 'Mali', 'MM': 'Myanmar', 'MN': 'Mongolia', 'MO': 'Macau', 'MP': 'Northern Mariana Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MS': 'Monserrat', 'MT': 'Malta', 'MU': 'Mauritius', 'MV': 'Maldives', 'MW': 'Malawi', 'MX': 'Mexico', 'MY': 'Malaysia', 'MZ': 'Mozambique', 'NA': 'Nambia', 'NC': 'New Caledonia', 'NE': 'Niger', 'NF': 'Norfolk Island', 'NG': 'Nigeria', 'NI': 'Nicaragua', 'NL': 'Netherlands', 'NO': 'Norway', 'NP': 'Nepal', 'NR': 'Nauru', 'NT': 'Neutral Zone (no longer exists)', 'NU': 'Niue', 'NZ': 'New Zealand', 'OM': 'Oman', 'PA': 'Panama', 'PE': 'Peru', 'PF': 'French Polynesia', 'PG': 'Papua New Guinea', 'PH': 'Philippines', 'PK': 'Pakistan', 'PL': 'Poland', 'PM': 'St. Pierre & Miquelon', 'PN': 'Pitcairn', 'PR': 'Puerto Rico', 'PS': 'Palestine', 'PT': 'Portugal', 'PW': 'Palau', 'PY': 'Paraguay', 'QA': 'Qatar', 'RE': 'RГ©union', 'RO': 'Romania', 'RS': 'Serbia', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'SA': 'Saudi Arabia', 'SB': 'Solomon Islands', 'SC': 'Seychelles', 'SD': 'Sudan', 'SE': 'Sweden', 'SG': 'Singapore', 'SH': 'St Helena', 'SI': 'Slovenia', 'SJ': 'Svalbard & Jan Mayen Islands', 'SK': 'Slovakia', 'SL': 'Sierra Leone', 'SM': 'San Marino', 'SN': 'Senegal', 'SO': 'Somalia', 'SR': 'Suriname', 'ST': 'Sao Tome & Principe', 'SU': 'Union of Soviet Socialist Republics (no longer exi', 'SV': 'El Salvador', 'SY': 'Syrian Arab Republic', 'SZ': 'Swaziland', 'TC': 'Turks & Caicos Islands', 'TD': 'Chad', 'TF': 'French Southern Territories', 'TG': 'Togo', 'TH': 'Thailand', 'TJ': 'Tajikistan', 'TK': 'Tokelau', 'TM': 'Turkmenistan', 'TN': 'Tunisia', 'TO': 'Tonga', 'TP': 'East Timor', 'TR': 'Turkey', 'TT': 'Trinidad & Tobago', 'TV': 'Tuvalu', 'TW': 'Taiwan, Province of China', 'TZ': 'Tanzania, United Republic of', 'UA': 'Ukraine', 'UG': 'Uganda', 'UM': 'United States Minor Outlying Islands', 'US': 'United States of America', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VA': 'Vatican City State (Holy See)', 'VC': 'St. Vincent & the Grenadines', 'VE': 'Venezuela', 'VG': 'British Virgin Islands', 'VI': 'United States Virgin Islands', 'VN': 'Viet Nam', 'VU': 'Vanuatu', 'WF': 'Wallis & Futuna Islands', 'WS': 'Samoa', 'XK': 'Kosovo', 'YD': 'Democratic Yemen (no longer exists)', 'YE': 'Yemen', 'YT': 'Mayotte', 'YU': 'Yugoslavia', 'ZA': 'South Africa', 'ZM': 'Zambia', 'ZR': 'Zaire', 'ZW': 'Zimbabwe'}

def reg_id(region_name):#перевод региона в номер
    if region_name in reg_id_sl:
        res = reg_id_sl[region_name]
    else:
        res = 'ERROR region'
    return str(res)

def sok_country(country_code):#перевод сокращения в страну
    if country_code in sok_country_sl:
        res = sok_country_sl[country_code]
    else:
        res = 'Undefined region'
    return str(res)

chet = 1 #счетчик - курсор по строке
with open("example.txt", "r") as example:
    with open("result.txt", "w+") as result:
        strexample = example.read()
        result.write("INSERT INTO marketing events.country_region \n(country_code, region_id, region_name, country_name) VALUES \n")
        while chet < len(strexample) - 2:
            numcou = strexample.find("==", chet) + 3 #страна начинается тут
            #numreg = min(strexample.find(",'", numcou) + 2, strexample.find(", '", numcou) + 3)
            nopr = strexample.find(",'", numcou)
            pr = strexample.find(", '", numcou)
            numreg = nopr + 2 if nopr < pr and nopr != -1 else pr + 3
            a = strexample.find(",'", numcou)
            b = strexample.find(", '", numcou)
            if strexample.find("==", chet) == -1:
                break
            country_code = strexample[numcou:numcou + 2]
            region_name = strexample[numreg:numreg + 2]
            if region_name == 'CI':
                region_name = 'CIS'
            elif region_name == 'Ot':
                region_name = 'Other'
            result.write("('" + country_code + "', " + reg_id(region_name) + ", '" + region_name + "', '" + sok_country(country_code) + "'),\n")

            chet = numcou + 10
    with open("result.txt", 'rb+') as result: # удаление последней
        result.seek(-2, os.SEEK_END)
        result.truncate()
