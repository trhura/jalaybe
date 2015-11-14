# Zawgyi<>Unicode converter python module
# Based on rules from Parabaik Myanmar Text Converter
# Copyright (C) 2014 Ngwe Tun (Solveware Solution)
# Copyright (C) 2014 Thura Hlaing

# This file is part of Paytan.

# Paytan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Paytan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import re

def zg12uni51(input_text=""):
    output_text = input_text
    output_text = re.sub(u'\u106a', u'\u1009', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1025(?=[\u1039\u102c])', u'\u1009', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1025\u102e', u'\u1026', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u106b', u'\u100a', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1090', u'\u101b', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1040', u'\u1040', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u108f', u'\u1014', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1012', u'\u1012', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1013', u'\u1013', output_text, flags=re.M|re.U)
    output_text = re.sub(u'[\u103d\u1087]', u'\u103e', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u103c', u'\u103d', output_text, flags=re.M|re.U)
    output_text = re.sub(u'[\u103b\u107e\u107f\u1080\u1081\u1082\u1083\u1084]', u'\u103c', output_text, flags=re.M|re.U)
    output_text = re.sub(u'[\u103a\u107d]', u'\u103b', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u103d\u103b', u'\u103b\u103e', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u108a', u'\u103d\u103e', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u103d\u103c', u'\u103d\u103e', output_text, flags=re.M|re.U)
    output_text = re.sub(u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])\u1064', u'\u1064\\1\\2\\3', output_text, flags=re.M|re.U)
    output_text = re.sub(u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])\u108b', u'\u1064\\1\\2\\3\u102d', output_text, flags=re.M|re.U)
    output_text = re.sub(u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])\u108c', u'\u1064\\1\\2\\3\u102e', output_text, flags=re.M|re.U)
    output_text = re.sub(u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])\u108d', u'\u1064\\1\\2\\3\u1036', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u105a', u'\u102b\u103a', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u108e', u'\u102d\u1036', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1033', u'\u102f', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1034', u'\u1030', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1088', u'\u103e\u102f', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1089', u'\u103e\u1030', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1039', u'\u103a', output_text, flags=re.M|re.U)
    output_text = re.sub(u'[\u1094\u1095]', u'\u1037', output_text, flags=re.M|re.U)
    output_text = re.sub(u'([\u1000-\u1021])([\u102c\u102d\u102e\u1032\u1036]){1,2}([\u1060\u1061\u1062\u1063\u1065\u1066\u1067\u1068\u1069\u1070\u1071\u1072\u1073\u1074\u1075\u1076\u1077\u1078\u1079\u107a\u107b\u107c\u1085])', u'\\1\\3\\2', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1064', u'\u1004\u103a\u1039', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u104e', u'\u104e\u1004\u103a\u1038', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1086', u'\u103f', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1060', u'\u1039\u1000', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1061', u'\u1039\u1001', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1062', u'\u1039\u1002', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1063', u'\u1039\u1003', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1065', u'\u1039\u1005', output_text, flags=re.M|re.U)
    output_text = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1068', u'\u1039\u1007', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1069', u'\u1039\u1008', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u106c', u'\u1039\u100b', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1070', u'\u1039\u100f', output_text, flags=re.M|re.U)
    output_text = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output_text, flags=re.M|re.U)
    output_text = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1075', u'\u1039\u1012', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1076', u'\u1039\u1013', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1077', u'\u1039\u1014', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1078', u'\u1039\u1015', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1079', u'\u1039\u1016', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u107a', u'\u1039\u1017', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u107b', u'\u1039\u1018', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u107c', u'\u1039\u1019', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1085', u'\u1039\u101c', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u106d', u'\u1039\u100c', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1091', u'\u100f\u1039\u100d', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1092', u'\u100b\u1039\u100c', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1097', u'\u100b\u1039\u100b', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u106f', u'\u100e\u1039\u100d', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u106e', u'\u100d\u1039\u100d', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(\u103c)([\u1000-\u1021])((?:\u1039[\u1000-\u1021])?)', u'\\2\\3\\1', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(\u103d)(\u103d)([\u103b\u103c])', u'\\3\\2\\1', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(\u103d)([\u103b\u103c])', u'\\2\\1', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(\u103d)([\u103b\u103c])', u'\\2\\1', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(?<=([\u1000-\u101c\u101e-\u102a\u102c\u102e-\u103d\u104c-\u109f]))(\u1040)(?=\s)?', u'\u101d', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(?<=(\u101d))(\u1040)(?=\s)?', u'\u101d', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(?<=([\u1000-\u101c\u101e-\u102a\u102c\u102e-\u103d\u104c-\u109f\s]))(\u1047)', u'\u101b', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(\u1047)(?=[\u1000-\u101c\u101e-\u102a\u102c\u102e-\u103d\u104c-\u109f\s])', u'\u101b', output_text, flags=re.M|re.U)
    output_text = re.sub(u'((?:\u1031)?)([\u1000-\u1021])((?:\u1039[\u1000-\u1021])?)((?:[\u102d\u102e\u1032])?)([\u1036\u1037\u1038]{0,2})([\u103b-\u103c]{0,3})((?:[\u102f\u1030])?)([\u1036\u1037\u1038]{0,2})((?:[\u102d\u102e\u1032])?)', u'\\2\\3\\6\\1\\4\\9\\7\\5\\8', output_text, flags=re.M|re.U)
    output_text = re.sub(u'\u1036\u102f', u'\u102f\u1036', output_text, flags=re.M|re.U)
    output_text = re.sub(u'(\u103a)(\u1037)', u'\\2\\1', output_text, flags=re.M|re.U)
    return output_text
