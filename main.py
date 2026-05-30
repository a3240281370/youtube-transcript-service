from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript')
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({'success': False, 'error': 'missing video_id'})
    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id, languages=['zh-TW', 'zh-CN', 'zh-Hans', 'zh'])
        text = ' '.join([t.text for t in transcript])
        return jsonify({'success': True, 'transcript': text})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
