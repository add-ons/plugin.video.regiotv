# -*- coding: utf-8 -*-
# Copyright: (c) 2020, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""Implementation of IPTVManager class"""

from __future__ import absolute_import, division, unicode_literals
from data import CHANNELS


class IPTVManager:
    """Interface to IPTV Manager"""

    @staticmethod
    def __init__():
        """Initialize IPTV Manager object"""

    def send_data(self, host, port, data):
        """Send data to IPTV Manager"""
        import json
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        try:
            sock.send(json.dumps(data))
        finally:
            sock.close()

    def channels(self, port):
        """Return JSON-M3U formatted information to IPTV Manager"""
        streams = []
        for channel in CHANNELS:
            if not channel.get('live_stream'):
                continue
            streams.append(dict(
                id=channel.get('website'),
                name='{name} ({label})'.format(**channel),
                logo=channel.get('logo'),
                stream=channel.get('live_stream'),
                radio=False,
            ))
        self.send_data('localhost', port, dict(version=1, streams=streams))
