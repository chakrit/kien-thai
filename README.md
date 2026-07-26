# เขียนไทย

**skill สอน Claude เขียนภาษาไทยให้คนไทยอ่านสบาย**

> ภาษาไทยที่ AI สร้างมีกลิ่น

คนไทยอ่านแล้วต้องย้อนอ่านใหม่ บางครั้งก็เลิกอ่านไปเลย ปัญหานี้ไม่ได้เกิดจากความรู้
ภาษาของ AI แต่เกิดจาก training data ที่เอนไปทางภาษาราชการและการแปลตรงตัวจากภาษา
อังกฤษ ผลคือประโยคยาว ๆ ต่อกันด้วย "ซึ่ง" กับ "โดย" ลงท้ายครับ/ค่ะ ทุกประโยค
ขึ้นต้นด้วย "ในยุคปัจจุบัน" ทุกบทความ

repo นี้รวบรวมกฎการเขียนภาษาไทยที่กลั่นจากนักเขียน blog สาย dev จริง บทความ explainer
ของธนาคารใหญ่ คอลัมนิสต์รุ่นใหม่ และนักแปลหนังสือสำนักพิมพ์รสนิยมดี ขึ้นรูปเป็น skill
สำหรับ Claude

ปลายทาง: ภาษาไทยที่อ่านลื่น มีน้ำเสียง และเลือกระดับได้ถูกบริบท

## เหมาะกับใคร

- developer ที่ใช้ AI เขียน technical doc / README / changelog ภาษาไทย
- ทีม content marketing ที่ต้องผลิตงานภาษาไทยเร็วและสม่ำเสมอ
- ใครก็ตามที่เคยเจอ output ภาษาไทยจาก AI แล้วตะหงิดใจ

## เริ่มใช้ยังไง

skill อยู่ที่ `skills/kien-thai/` ให้ copy ทั้ง folder ไปไว้ใน `.claude/skills/`
ของ project ที่ต้องการ หรือ import ผ่านระบบ skill management ที่คุณใช้อยู่

(ตัวอย่าง: ใน [ACE](https://github.com/ace-rs/ace) ใช้ `ace import skills/kien-thai`
จาก clone ของ repo นี้)

## ใช้แบบ audit loop

วิธีใช้ skill ที่ได้ผลที่สุดคือ audit loop ให้ Claude ตรวจงานเขียนเทียบกฎทีละรอบ
trace ก่อนแก้ทุกจุด วนใหม่จนกว่าจะไม่เจออะไรเพิ่ม (รายละเอียดในส่วน
"วินัยการเพิ่มกฎ")

ตัวอย่าง prompt ที่ใช้ได้เลย:

```
แก้ไฟล์นี้โดยอ้างอิงกับสกิล kien-thai แก้ไปเรื่อยๆ แก้เสร็จวนตรวจทานซ้ำใหม่
วนอ่านตรวจสอบแล้วแก้ไปเรื่อยๆ อย่าหยุดจนกว่าจะไม่เจอจุดผิดพลาดใดๆ ให้แก้อีก
```

หรือใช้ skill `kode-thai` (โคตรไทย) ที่เก็บคำสั่งนี้ไว้ให้แล้ว เรียกผ่าน
`/kode-thai` หรือบอกเป็นภาษาไทยว่า "ตรวจวนๆ จนกว่าจะหมดที่ผิด" ก็ได้

ระวัง audit loop กิน token หนัก skill มี SKILL.md + 8 reference รวมหลายหมื่น token
ถ้าตรวจงานเขียนยาว ๆ หลายรอบ ค่าใช้จ่ายบวมเร็ว เตรียมงบ context ไว้ให้พอ
(harness scope register ก่อนยิง เพื่อตัดส่วนที่ไม่ใช้ออก เหลือประมาณครึ่งหนึ่ง)

## หลักคิดของ skill

skill นี้ไม่ได้เป็นแค่ checklist ของคำต้องห้าม แกนกลางคือ **กรอบการเรียบเรียง 7
ข้อ** ที่อธิบายว่าภาษาไทยจัดอนุประโยค จัดประโยค จัดย่อหน้า ต่างจากภาษาอังกฤษยังไง
พอกรอบถูก กฎปลีกย่อยส่วนใหญ่ก็ตามมาเอง

1. **ยกประเด็นนำหน้า ไม่ใช่ประธานนำหน้า** — ภาษาไทยยกสิ่งที่ประโยคพูดถึงขึ้นก่อน
   ไม่ลากประธานหนัก ๆ มาวางหน้าเหมือนภาษาอังกฤษ
2. **เงื่อนไข เวลา กรอบ มาก่อน** — ข้อมูล setup วางหน้าประโยคหลัก ไม่ใช่ห้อย
   ท้ายด้วย "เมื่อ..." แบบภาษาอังกฤษ
3. **เว้นวรรค + ขึ้นย่อหน้าแทนมหัพภาค** — ภาษาไทยไม่ลงจุดทุกประโยคแบบภาษาอังกฤษ
   ขอบเขตประโยคใช้ space กับการขึ้นย่อหน้า
4. **ปิดประโยคด้วยคำลงท้าย** — ด้วย แล้ว เลย ไป ไม่ใช่จุด ไม่ใช่ "ทั้งนี้" ลอย ๆ
5. **เชื่อมประโยคด้วยการละประธาน + คำชี้เฉพาะ** — ละประธานที่รู้แล้ว ไม่ใช่
   ลาก "ซึ่ง" ต่อกันสามชั้น
6. **ใช้ "ก็" คุมจังหวะ** — คำเสริมที่ภาษาอังกฤษไม่มี ใช้คุมจังหวะประโยคและบ่ง
   ความสัมพันธ์หลวม ๆ ระหว่างอนุประโยค
7. **เปลี่ยนหัวข้อด้วยคำถามเชิงวาทศิลป์** — ขยับหัวข้อย่อยด้วย "แล้วถ้า..."
   แทนการใช้ "อย่างไรก็ตาม" / "นอกจากนี้"

แต่ละกรอบใน `SKILL.md` ลิงก์ไปยัง anti-pattern ที่เกี่ยวข้อง

## โครงสร้าง skill

| ไฟล์                            | เนื้อหา                                              |
| ------------------------------- | --------------------------------------------------- |
| `SKILL.md`                      | กรอบการเรียบเรียง 7 ข้อ + person deixis + workflow   |
| `references/ai-tells.md`        | กฎ mechanical: connective spam ถูก- passive padding |
| `references/grammar.md`         | surface grammar: ลักษณนาม modal function-word verb  |
| `references/craft.md`           | taste/voice: headline cliché closing intensifier    |
| `references/style-rules.md`     | กฎเชิงบวก + ทับศัพท์ 4-bucket judgment              |
| `references/register.md`        | 6 register family + person deixis + voice attrs    |
| `references/examples.md`        | ตัวอย่าง before/after register-tagged               |
| `references/exemplars.md`       | native corpus excerpts, pinned last in bundle       |
| `references/forbidden-phrases.md` | blocklist สำหรับ audit pre-check                 |

skill โหลด `SKILL.md` เป็น context หลัก แล้วอ่าน reference อื่น ๆ เมื่อจำเป็น
ค่อย ๆ เปิดทีละชั้น

## Eval ทำงานยังไง

repo นี้ไม่ได้มากับกฎอย่างเดียว แต่มาพร้อม harness ที่ใช้ pytest ผูก `claude` กับ
`codex` ใน bare mode รันคู่กันเพื่อเทียบผลก่อนกับหลัง inject skill อีกขาหนึ่งเป็น
Typhoon โมเดลที่เทรนภาษาไทยมาแต่ต้น รันในเครื่องผ่าน ollama ให้ร่างต้นฉบับออกมา
แล้วเอามาวางเทียบกับขาของ `claude`

```bash
uv sync
uv run pytest                       # sanity เร็ว ๆ ไม่เรียก API
uv run pytest -m generate           # ยิงจริง ใช้ token จริง
uv run pytest -m generate -k claude # เลือก backend เดียว
uv run pytest -m evaluate           # ตรวจหยาบเชิงปริมาณ (เป็นแค่สัญญาณ)
uv run pytest -m recall             # วัด recall ของ auditor (ช้า ใช้ token)

# ขา Typhoon + สร้างไฟล์เทียบสองขา
EVAL_ITERATION=15 uv run python tests/generate/typhoon_pass.py
uv run python tests/generate/compare_arms.py iteration-15
```

เวลารันหลายขาพร้อมกัน ให้ตั้ง environment variable `EVAL_ITERATION` เพื่อ pin ให้
ทุกขาเขียนลง iteration เดียวกัน ถ้าไม่ตั้ง แต่ละขาจะสร้าง iteration ของตัวเองแยกกัน
พอเป็นคนละรอบคนละสถานะ skill ก็เอามาเทียบกันไม่ได้

artifact จะลงที่ `workspace/iteration-N/<eval>/<backend>/<config>/`
จากนั้นดูผลกับ Claude ใน chat ได้เลย ไม่มี viewer แยกต่างหาก

สารบบของทุก iteration อยู่ที่ [`workspace/INDEX.md`](workspace/INDEX.md) — สร้าง iteration
ใหม่เมื่อไรให้เพิ่มแถว และอัปเดตช่อง Review เมื่อ review เสร็จ

การตัดสินคุณภาพงานเขียนเป็นงานของมนุษย์ ส่วน `test_quant.py` แค่ flag คำต้องห้าม
และตำแหน่งที่คำเชื่อมแน่นเกิน ไม่ใช่ด่านตัดสินคุณภาพ

## วินัยการเพิ่มกฎ

ทุกกฎใน `references/` มีที่มาจากการค้นคว้างานเขียนจริง ไม่ใช่จากความรู้สึก เวลา
eval ออกมาไม่ดี ขั้นตอนคือ:

1. หา pattern ที่ผิดใน output
2. map กลับไปยังกฎที่ควรจับได้ ถ้ามีแต่ไม่ทำงาน ก็แก้ถ้อยคำ / ความเด่นของกฎเดิม
3. ถ้าไม่มีกฎครอบคลุม เช็คงานค้นคว้าก่อน มีหลักฐานไหม ถ้าไม่มี กฎใหม่ก็เป็นแค่
   ข้อสันนิษฐาน ต้อง flag และถือเป็นกฎชั่วคราว
4. log ที่มาไว้ใน `iteration-N/feedback.md`

อ่านรายละเอียดใน `CLAUDE.md` ส่วน "Iteration discipline"

## ที่มาของกฎทุกข้อ

ทุกกฎใน skill นี้กลั่นจากตัวอย่างงานเขียนจริง:

- **blog dev ไทย** — Blognone long-form, Somkiat Puisungnoen, Thanaphoom Babparn,
  Nutta, Rath Panyowat
- **บทความ explainer สายการเงิน** — Krungsri The COACH, ttb fin tips, SCB Stories & Tips,
  KBank The Wisdom
- **newspaper รุ่นใหม่** — The Standard, The MATTER, The 101 World, Workpoint Today
- **งานแปล non-fiction** — Bookscape, openworlds, Salt Publishing,
  สฤณี อาชวานันทกุล

ในรายการนี้ไม่มีคอลัมนิสต์ดัง ๆ คนไหน ก็เป็นความตั้งใจ กฎควรครอบคลุมงานเขียน
คุณภาพทั่วไป ไม่ใช่ลอกเสียงใครคนเดียว

## สถานะ

ตอนนี้รันมาถึง iteration ที่ 15 กรอบการเรียบเรียง 7 ข้อกับกฎปลีกย่อยผ่าน eval
มาหลายรอบแล้ว คำถามที่ยังเปิดค้างอยู่คือ ระหว่างให้โมเดลที่เทรนไทยมาร่างก่อน
กับให้ Claude ร่างพร้อม skill อันไหนได้น้ำเสียงเป็นธรรมชาติกว่ากัน และคำตอบต้อง
ตัดสินด้วยหูของเจ้าของภาษา ไม่ใช่ตัวเลข

ใครเจอกฎที่พลาดหรือผิด เปิด issue หรือ PR ได้ ดูขั้นตอน + รูปแบบ slug ใน
[`CONTRIBUTING.md`](CONTRIBUTING.md)

## License

[MIT](LICENSE) ใช้ได้อิสระทั้งงานส่วนตัวและงานเชิงพาณิชย์ ขอแค่เก็บ copyright
notice ไว้
