# Contributing

ขอบคุณที่คุณอยากจะช่วยปรับปรุง skill นี้ เอกสารนี้สรุปขั้นตอนการเสนอการแก้ไขเมื่อเจอกฎที่ผิด เจอ AI tell ที่ skill จับไม่ได้ หรืออยากเพิ่มกฎใหม่

## 0. อ่านก่อน

ก่อนเปิด issue หรือ PR ขอให้อ่านสามไฟล์นี้ก่อน:

1. [`skills/kien-thai/SKILL.md`](skills/kien-thai/SKILL.md): กรอบการเรียบเรียง
   7 ข้อ + person deixis + workflow
2. [`skills/kien-thai/references/register.md`](skills/kien-thai/references/register.md):
   register 6 family
3. ไฟล์ใน `references/` ที่ตรงกับประเภทกฎ: `ai-tells.md` (mechanical),
   `grammar.md` (surface), `craft.md` (taste), `style-rules.md` (positive)

feedback ในลักษณะ "กฎข้อนี้ผิด" จริง ๆ แล้วส่วนใหญ่จะเป็น register-mismatch มากกว่า ไม่ใช่ตัวกฎพัง ลองเช็คดูก่อนว่ากำหนด register ถูกต้องแล้วหรือยัง

## 1. วินัยการเพิ่มกฎ — trace before you write

ทุกกฎใน skill นี้กลั่นจากงานเขียนจริง (tech blog, bank long-form, newspaper รุ่นใหม่, งานแปลฝีมือดี) มี *why* รองรับทุกข้อ คือ failure mode ที่ไม่ต้องการให้เกิดขึ้น หรือ pattern ของมนุษย์ที่อยากให้ทำตาม

**กฎที่ไม่มีที่มาจะเน่า** อย่ารีบเพิ่มกฎเร็วกว่าเพิ่มหลักฐาน

เวลาเจอ output แย่ ๆ ความรู้สึกแรกคืออยากจะเพิ่มกฎใหม่ หรือเพิ่มความเข้มงวดของกฎเดิม **อดทนไว้** อย่าเพิ่งรีบเพิ่ม ทำตาม trace ก่อน:

1. **หา offending pattern** ใน output ที่เป็นปัญหา
2. **map กลับไปยังกฎที่ควรจับได้** ถามว่ากฎไหน ไฟล์ไหนก่อน ถ้าไม่เจอถึงจะเป็นช่องโหว่จริง
3. **ถ้ากฎมีอยู่แล้วแต่ไม่ทำงาน** ตรวจดูก่อนว่าเพราะอะไร wording อ่อนรึเปล่า? ตัวอย่างไม่ชัดใช่ไหม? หรือว่ามันขัดกับกฎอื่น? register ไม่ตรง? **แก้กฎเดิมให้ดีขึ้นก่อนโดยการปรับ wording / ความเด่น / anchoring example ก่อน อย่าซ้อนกฎใหม่ที่พูดเรื่องเดียวกัน**
4. **ถ้าไม่มีกฎครอบคลุมจริง ๆ** ก่อนจะเพิ่ม ลองค้นหางานค้นคว้าที่มีอยู่ก่อน ว่า pattern นี้มีการศึกษา หรือตัวอย่างที่เห็นได้ชัดในงานจริงที่คนเขียนไหม ถ้ามี ก็ดึงขึ้นมาเขียนเป็นกฎ ถ้าไม่มี กฎใหม่ก็จะเป็นได้แค่ข้อสันนิษฐานเท่านั้น ต้อง flag ให้เป็น provisional แล้ว cite counter-example หรือแหล่งที่มาให้ชัด
5. **บันทึก trace** ใน issue / PR description เพื่อให้ข้อมูลที่มาของกฎอยู่ใกล้กับ diff ของการแก้ไขกฎนั้น ๆ มากที่สุด

สามารถอ่านขั้นตอนรายละเอียดเดียวกันนี้เพิ่มเติมจาก CLAUDE.md ส่วน "Iteration discipline" ได้

## 2. ขั้นตอนเสนอแก้ไข

ให้ใช้ template ตามนี้ใน issue / PR:

### a. ระบุ register

prose ตัวอย่างเป็น register ไหน?

- `explainer`: bank/tech long-form
- `marketing-saas-sme` / `marketing-b2b-formal` / `marketing-fintech-warm` /
  `marketing-retail-tech`: Marketing 4 sub-register
- `personal-blog`: dev blog / war-story
- `news`: ข่าว / reference doc
- `academic`: วิชาการยาว
- `official`: meeting minutes / government memo (provisional)

ถ้า register ไม่ตรงกับที่ skill จับ แจ้งได้เลยว่าควรเป็น register ไหน หรือ skill เข้าใจผิดยังไง

### b. ระบุลำดับชั้นของกฎ

ระบุก่อนว่า issue เป็นเรื่องอะไร:

- **discourse-level**: โครงสร้างประโยค การจัดอนุประโยค การเปลี่ยน topic
  → frame F1–F7 ใน SKILL.md
- **mechanical**: ตัวเชื่อมเฝือ คำแปลตรงตัว passive ใช้ผิด
  → `ai-tells.md`
- **surface grammar**: ลักษณนาม modal classifier function-word
  → `grammar.md`
- **taste / voice**: headline ซ้ำซาก closing แบบ recap empty intensifier
  → `craft.md`
- **positive guidance**: สิ่งที่อยากให้ทำตอน draft ไม่ใช่กฎ audit
  → `style-rules.md`

ถ้าหากไม่แน่ใจก็เดามาก่อนได้ เดี๋ยว reviewer จะช่วยปรับให้

### c. trace

- กฎไหน *น่าจะ* จับ pattern นี้ได้? cite slug ของกฎ
- ทำไมกฎไม่ทำงาน? วิเคราะห์ดูว่าเป็นเพราะ wording อ่อน / ตัวอย่างเก่า / ขัด register / ตัวกฎไม่มีจริง หรือเพราะอย่างอื่น?
- เสนอการแก้ไข: rewrite กฎเดิม หรือเพิ่ม slug ใหม่

### d. ที่มา (กรณีเสนอกฎใหม่)

cite ตัวอย่างจริงอย่างน้อยหนึ่งแหล่ง:

- blog dev ไทย / bank explainer / newspaper รุ่นใหม่ / งานแปล non-fiction พร้อม URL หรือ excerpt
- หรือ counter-example ชัด ๆ ที่แสดงว่ากฎเดิมพลาด

กฎที่ไม่มี citation จะเข้าเป็น *provisional* คือมี marker ใน file รอ eval หลายรอบเพื่อยืนยัน

## 3. รูปแบบ slug + metadata

ทุกกฎมี heading รูปนี้:

```markdown
### `<slug>` *(<type> · <scope> · <severity>)*

<body — คำอธิบาย + Bad/Good example>
```

- **slug**: kebab-case อ่านได้ ใช้ romanization ของคำหลัก ถ้าเป็นคำ Thai
  (`chueung-stacking`, `mi-khwam-padding`) หรือชื่อ pattern ตรง ๆ ถ้าไม่มี Thai
  หลัก (`em-dash-semicolon`, `wrong-classifier`)
- **type**: `mechanical` / `grammar` / `craft` / `style` / `frame`
- **scope**: `all-registers` / `scoped` / `<register-key>` (เช่น `marketing`,
  `register`)
- **severity**: `hard` (กฎ correctness) / `soft` (taste) / `structural` (frame)

frame slug ใช้ form `f<N>` (`f1`...`f7`) sub-pattern ใต้ frame ใช้
`f<N>/<descriptor>` (เช่น `f4/targhak-closure`)

cross-reference ระหว่าง rule ให้ใช้ slug ใน backtick ใส่ไปในเนื้อความ เช่น "ดู `mid-paragraph-period` สำหรับ period spam"

## 4. รูปแบบ PR

- **title** หัวข้อสั้น ๆ ระบุประเภท + slug ที่กระทบ เช่น `craft: rewrite cliche-headline to cover SEO listicle pattern` หรือ `ai-tells: add new slug for X`
- **body** ต้องครอบคลุม:
  - register และไฟล์กฎที่กระทบ
  - offending example (snippet จริง)
  - trace ตามข้อ 2 ข้างบน
  - diff ของ rule wording (ถ้าแก้กฎเดิม) หรือ slug + metadata + body ใหม่ (ถ้าเพิ่มกฎใหม่)
  - citation
- **scope** หนึ่ง logical change ต่อ PR อย่ารวมแก้กฎหลายข้อใน PR เดียว ยกเว้นเป็นการ refactor โครงสร้างขนานใหญ่

## 5. eval expectations

การแก้กฎมักทำให้ behavior model เปลี่ยน เพราะฉะนั้นก่อน submit รบกวนรัน eval รอบใหม่ให้หน่อยนะครับ

ก่อน merge:

```sh
uv sync
uv run pytest                  # sanity (ฟรี)
uv run pytest -m generate      # full eval (ใช้ API token)
```

นอกจาก pytest สองคำสั่งหลัก ถ้าจะรันหลายขาเทียบกันอย่าลืม pin ด้วย
`EVAL_ITERATION` ขั้นตอนเต็มดูได้ที่
[`docs/guides/running-evals.md`](docs/guides/running-evals.md)

เก็บผลไว้ที่ `workspace/iteration-N/`

ทุกครั้งที่สร้าง iteration ใหม่ ให้เพิ่มแถวใน [`workspace/INDEX.md`](workspace/INDEX.md)
(วันที่ + mode/scope, ช่อง Review = `pending`) และเมื่อ review เสร็จก็เปลี่ยนช่องนั้นเป็น
`reviewed` พร้อมลิงก์ไป feedback ตาราง INDEX คือสารบบของ iteration ทั้งหมด ถ้าไม่อัปเดตก็จะบอกสถานะ repo ผิด

ถ้าไม่มี API key หรือ codex setup ก็ไม่เป็นไร แจ้งมาใน issue/PR แล้วเดี๋ยวทางเรา run ให้เอง

## 6. สิ่งที่เกินขอบเขต (ตอนนี้)

- LLM-judge eval: ใช้ human review จนกว่าจะพิสูจน์ได้ว่า LLM ทำงานดีกว่าคน
- กฎที่อ้างอิงคอลัมนิสต์ดังคนเดียว: skill ควรครอบคลุม pattern ที่ใช้ได้สำหรับคนทั่วไป ไม่ใช่การลอกน้ำเสียงของคน คนใดคนหนึ่ง