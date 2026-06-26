# -*- coding: utf-8 -*-
import json

log_path = r"C:\Users\Paul\.gemini\antigravity\brain\c54152f5-3cfa-4430-93ae-f360ed9f4b15\.system_generated\logs\transcript_full.jsonl"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get('step_index')
            if 930 <= step <= 943:
                source = data.get('source')
                type_ = data.get('type')
                print(f"[{step}] Source: {source}, Type: {type_}")
                if type_ == 'USER_INPUT':
                    print(f"      Content: {data.get('content', '')[:300]}")
                elif source == 'MODEL':
                    tool_calls = data.get('tool_calls', [])
                    if tool_calls:
                        print(f"      Tools: {[{tc.get('name'): tc.get('arguments')} for tc in tool_calls]}")
                    if data.get('content'):
                        print(f"      Response: {data.get('content')[:500]}")
        except Exception as e:
            pass
